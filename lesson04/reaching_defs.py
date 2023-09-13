import json
import sys
import worklist as w

def merge(mergeList):
  mergeSet = {}
  for set in mergeList:
    mergeSet = mergeSet.union(set)
  return mergeSet

def transfer(b, ins):
  return w.definitions(b).union(ins.difference(w.kills(b)))

init = {}
direction = w.Direction.FORWARD

program = json.load(sys.stdin)
for func in program['functions']:
  worklist = w.Worklist(func, init, merge, transfer, direction)
  ins, outs = worklist.worklist()


