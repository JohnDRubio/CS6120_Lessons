from enum import Enum
from cfg import formBasicBlocks, createCFG, buildPredecessorMap
import json
import sys

DIRECTION = ("FORWARD", "BACKWARD")

class WorkList:
  def __init__(self, insns, merge, transfer, direction):
      self.insns = insns
      self.merge = merge
      self.transfer = transfer
      self.direction = direction
      self.cfg = {}
      self.basicBlocks = []
      self.setup()

  def setup(self):
    self.basicBlocks = formBasicBlocks(self.insns)
    self.cfg = createCFG(self.basicBlocks)[0]
    self.predecessorMap = buildPredecessorMap(self.cfg)

  def worklistAlgo(self):
    ins = {}    # {label0 : {a : 0, b:1}, label1 : {b:1, c:2}}
    outs = {}
    worklist = set()

    for label in self.cfg:
        worklist.add(label)

    while len(worklist) != 0:
       blockLabel = worklist.pop()
       ins[blockLabel] = self.merge(self.predecessorMap[blockLabel], outs)
       prevOuts = outs[blockLabel] if blockLabel in outs else {}
       outs[blockLabel] = self.transfer(self.getBlock(blockLabel), blockLabel, ins[blockLabel])
       if prevOuts != outs[blockLabel]:
          thisBlocksSuccessors = self.getSuccessors(blockLabel)

          for successor in thisBlocksSuccessors:
             worklist.add(successor) 
    
    return ins, outs

  def getBlock(self, b_label):
    for block in self.basicBlocks:
      if block[0]['label'] == b_label:
        return block
    return None
  
  def getSuccessors(self, block):
    if block not in self.cfg:
      return []
    return self.cfg[block]

def getDefs(block):
    defs = {}   # map of varName -> value
    for insn in block:
      if 'dest' in insn:
        if 'value' in insn:
          defs[insn['dest']] = (insn['op'], insn['value'])
        else:
          defs[insn['dest']] = (insn['op'], insn['args'])
    return defs

def getKills(block, ins):
   defs = getDefs(block)
   kills = []
   for varName in defs:
       if varName in ins:
           kills.append(varName)
   return kills

# predecessors is a list of labels
# outs is a map from predecessor to the list of definitions that block's transfer
#    function returns
# returns a map of from varName to value at the entrance to this block
def reachingDefsMerge(predecessors, outs):
   merged = {}   # {varName -> [list of values from all predecessor blocks]}
   for predecessor in predecessors:
       if predecessor not in merged and predecessor in outs:
           merged[predecessor] = [outs[predecessor]]    
       else:
           if predecessor in outs:
            merged[predecessor].append(outs[predecessor])
   return merged

def reachingDefsTransfer(block, blockLabel, ins):
   defs = getDefs(block)
   kills = getKills(block, ins)
   result = {}

   for killedDef in kills:
      if killedDef not in ins[blockLabel]:
         for varName in ins[blockLabel]:
            if varName not in result:
               result[varName] = [ins[blockLabel][varName]]
            else:
               result[varName].append(ins[blockLabel][varName])
    
   for varName in defs:
      if varName not in result:
               result[varName] = [defs[varName]]
      else:
               result[varName].append(defs[varName])

   return result

     
if __name__ == "__main__":
    # program = json.load(sys.stdin)
    data = open('C:\\Users\\rubio\\Documents\\personal\\School\\CS6120\\lessons\\CS6120_Lessons\\lesson04\\reaching_def_test2.json')
    program = json.load(data)
    for func in program['functions']:
        workListResult = WorkList(func['instrs'], reachingDefsMerge, reachingDefsTransfer, DIRECTION[1])
        # print(str(workListResult.predecessorMap))
        workListResult.worklistAlgo()