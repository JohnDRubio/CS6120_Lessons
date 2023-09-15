from enum import Enum
from cfg import formBasicBlocks, createCFG

class Direction(Enum):
  FORWARD = 1
  BACKWARD = 2

class Worklist:
  def __init__(self, function, init, merge, transfer, direction):
      self.init = init
      self.merge = merge
      self.transfer = transfer
      self.direction = direction
      self.function = function
      self.basicBlocks = []
      self.cfg = {}
      self.predecessors = {}
      self.availableDefinitions = {}

  def setup(self):
    self.basicBlocks = formBasicBlocks(self.function['instrs'])
    self.cfg = createCFG(self.basicBlocks)[0]
    self.predecessors = self.buildPredecessorList()

  def buildPredecessorList(self):
    predecessors = {}
    for label in self.cfg:
      for successor in self.cfg[label]:
        if successor in predecessors:
          predecessors[successor].append(label)
        else:
          predecessors[successor] = [label]
    return predecessors

  def defs(self, b_label):
    defs = {}
    block = self.getBasicBlock(b_label)
    for insn in block:
      if 'dest' in insn:
        if 'value' in insn:
          defs[insn['dest']] = (insn['op'], insn['value'])
        else:
          defs[insn['dest']] = (insn['op'], insn['args'])
    return defs

  def kills(self, b_label):
    kills = {}
    defs = self.defs(b_label)
    for var, value in defs.items():
      if var in self.availableDefinitions:
        kills[var] = self.availableDefinitions[var]
      self.availableDefinitions[var] = value
    return kills

  def getSuccessors(self, block):
    if block not in self.cfg:
      return []
    return self.cfg[block]

  def getPredecessors(self, block):
    if block not in self.predecessors:
      return []
    return self.predecessors[block]

  def getBasicBlock(self, b_label):
    for block in self.basicBlocks:
      if block[0]['label'] == b_label:
        return block
    return None

  def worklist(self):
    self.setup()
    ins = {}
    outs = {}
    worklist = []
    for label in self.cfg:
      ins[label] = self.init
      outs[label] = self.init
      worklist.append(label)

    while len(worklist) != 0:
      b_label = worklist.pop(0)
      mergeList = []
      for pred in self.getPredecessors(b_label):
        mergeList.append(outs[pred])
      ins[b_label] = self.merge(mergeList)
      prevOut = outs[b_label]
      outs[b_label] = self.transfer(b_label, ins[b_label])
      if prevOut != outs[b_label]:
        for s in self.getSuccessors(b_label):
          if s not in worklist:
            worklist.append(s)

    return ins, outs