import lesson02 as blocks
import json
import sys

def getSuccessors(b):
  return cfg[b]

def getPredecessors(b):
  return predecessors[b]

def buildPredecessorList(cfg):
  predecessors = {}
  for label in cfg:
    for successor in cfg[label]:
      if successor in predecessors:
        predecessors[successor].append(label)
      else:
        predecessors[successor] = [label]
  return predecessors

def getBasicBlock(b_label):
  for block in basicBlocks:
    if block[0]['label'] == b_label:
      return block
  return None

def worklist(transfer, init, merge, direction):
  ins = {}
  outs = {}
  worklist = []
  for label in cfg:
    ins[label] = init # TODO: algorithm only says entry block gets set to init
    outs[label] = init
    worklist.append(label)

  while len(worklist) != 0:
    b_label = worklist[0]
    mergeList = []
    for pred in getPredecessors(b_label):
      mergeList.append(outs[pred])
    ins[b_label] = merge(mergeList)
    outs[b_label] = transfer(b_label, ins[b_label])

  return ins, outs


program = json.load(sys.stdin)
for func in program['functions']:
  basicBlocks = blocks.formBasicBlocks(func['instrs'])
  cfg = blocks.createCFG(basicBlocks)
  predecessors = buildPredecessorList(cfg)
  ins, outs = worklist(-1, -1, -1, -1) # TODO: implement functions to pass into worklist