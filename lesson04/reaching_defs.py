import json
import sys
import worklist as w

def merge(mergeList):
  mergeDict = {}
  for dict in mergeList:
    for key, value in dict.items():
      if key in mergeDict:
        mergeDict[key].append(value)
      else:
        mergeDict[key] = [value]
  return mergeDict

def transfer(b, ins):
  transfer = {}
  kills = worklist.kills(b)
  defs = worklist.defs(b)
  for varIn, valueIn in ins.items():
    if varIn in kills:
      transfer[varIn] = [x for x in valueIn if x not in kills[varIn]]
    else:
      transfer[varIn] = valueIn
  for varDef, valueDef in defs.items():
    if varDef not in transfer:
      transfer[varDef] = valueDef
    else:
      transfer[varDef] = list(set(transfer[varDef]) | set(valueDef))

  return transfer

init = {}
direction = w.Direction.FORWARD

program = json.load(sys.stdin)
for func in program['functions']:
  worklist = w.Worklist(func, init, merge, transfer, direction)
  ins, outs = worklist.worklist()
  print(func)
  print('\n')
  print(ins)
  print('\n')
  print(outs)


