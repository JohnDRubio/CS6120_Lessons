import json
import sys
import worklist as w

def ourExtend(l1,l2):
  copyL2 = l2.copy()
  for item in copyL2:
    l1.append(item)

def merge(mergeList):
  mergeDict = {}
  copyMergeList = mergeList.copy()
  for dict in copyMergeList:
    for key, value in dict.items():
      if key in mergeDict:
        print ("key: "+key+", value: "+str(value)+", mergeDict[key]: "+str(mergeDict[key]))
        print(id(mergeDict[key]))
        ourExtend(mergeDict[key], value)
      else:
        mergeDict[key] = value
  return mergeDict

def transfer(b, ins):
  transfer = {}
  kills = worklist.kills(b,ins)
  defs = worklist.defs(b)
  for varIn, valueIn in ins.items():
    if varIn not in kills:
      transfer[varIn] = valueIn
  for varDef, valueDef in defs.items():
    transfer[varDef] = [valueDef]

  return transfer

init = {}
direction = w.Direction.FORWARD

# program = json.load(sys.stdin)
data = open('C:\\Users\\rubio\\Documents\\personal\\School\\CS6120\\lessons\\CS6120_Lessons\\lesson04\\reaching_def_test2.json')
program = json.load(data)
for func in program['functions']:
  worklist = w.Worklist(func, init, merge, transfer, direction)
  ins, outs = worklist.worklist()
  # print('func\n')
  # print(func)
  # print('ins\n')
  # print(ins)
  # print('outs\n')
  # print(outs)


