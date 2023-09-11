import lesson02 as blocks
import json
import sys

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
    ins[b_label] = {} # TODO: calculate
    outs[b_label] = {} # TODO: calculate

  return ins, outs

def getSuccessor(b):
  return cfg[b]

def getPredecessor(b):
  return predecessors[b]

def getPredecessors(cfg):
  predecessors = {}
  for label in cfg:
    for successor in cfg[label]:
      if successor in predecessors:
        predecessors[successor].append(label)
      else:
        predecessors[successor] = [label]
  return predecessors


program = json.load(sys.stdin)
for func in program['functions']:
  basicBlocks = blocks.formBasicBlocks(func['instrs'])
  cfg = blocks.createCFG(basicBlocks)
  predecessors = getPredecessors(cfg)
  ins, outs = worklist(-1, -1, -1, -1)