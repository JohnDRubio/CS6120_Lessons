import json
import sys

# cfg is a map from label to list of successor labels
#   Example: {startLabel : [label2, label3]}
def buildPredecessorMap(cfg):
    # Basically a reverse cfg: map from label to list of its predecessors
    predecessors = {}
    for label in cfg:
        for successorLabel in cfg[label]:
            if successorLabel in predecessors:
                predecessors[successorLabel].append(label)
            else:
                predecessors[successorLabel] = [label]
    return predecessors


def formBasicBlocks(insns):
    basicBlocks = []
    currBlock = []
    for i in insns:
        if 'label' in i:
            basicBlocks.append(currBlock)
            currBlock = []
            currBlock.append(i)
        elif i['op'] == 'br' or i['op'] == 'jmp' or i['op'] == 'ret':
            currBlock.append(i)
            basicBlocks.append(currBlock)
            currBlock = []
        else:
            currBlock.append(i)
    basicBlocks.append(currBlock)
    basicBlocks = removeEmptyBasicBlocks(basicBlocks)
    basicBlocks = addLabels(basicBlocks)
    return basicBlocks

def addLabels(basicBlocks):
    num = 0
    for block in basicBlocks:
        if 'label' not in block[0]:
            block.insert(0,{"label": "label_"+str(num)})
            num = num + 1
    return basicBlocks

def removeEmptyBasicBlocks(basicBlocks):
    newBasicBlocks = [x for x in basicBlocks if x != []]
    return newBasicBlocks

def createCFG(basicBlocks):
    cfg = {}
    terminators = []
    for i,block in enumerate(basicBlocks):
        label = block[0]['label']
        lastInstr = block[-1]
        if 'label' in lastInstr:
            continue
        elif lastInstr['op'] == 'br' or lastInstr['op'] == 'jmp':
            cfg[label] = lastInstr['labels']
            terminators.append(lastInstr['op'])
        else:
            if i < len(basicBlocks) - 1 and lastInstr['op'] != 'ret': # make this change in lesson02
                cfg[label] = [basicBlocks[i+1][0]['label']]
                terminators.append('fall-through')
            else:
                cfg[label] = []
    return cfg, terminators