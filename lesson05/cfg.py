import json
import sys

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

def dfs(visited, cfg, node, nodes):
    if node not in visited:
        nodes.add(node)
        visited.add(node)
        for child in cfg[node]:
            dfs(visited,cfg,child,nodes)
    return nodes

def reduceCFG(cfg):
    start = list(cfg.keys())[0]
    reachableNodes = dfs(set(),cfg,start, set())

    for node in cfg.copy():
        if node not in reachableNodes:
            del cfg[node]

def createCFG(insns):
    basicBlocks = formBasicBlocks(insns)
    cfg = {}
    for i,block in enumerate(basicBlocks):
        label = block[0]['label']
        lastInstr = block[-1]
        if 'label' in lastInstr:
            if i < len(basicBlocks) - 1:
                cfg[label] = [basicBlocks[i+1][0]['label']]
            else:
                cfg[label] = []
        elif lastInstr['op'] == 'br' or lastInstr['op'] == 'jmp':
            cfg[label] = lastInstr['labels']
        else:
            if i < len(basicBlocks) - 1 and lastInstr['op'] != 'ret':
                cfg[label] = [basicBlocks[i+1][0]['label']]
            else:
                cfg[label] = []
    reduceCFG(cfg)
    return cfg

def buildPredecessorList(cfg):
    predecessors = {}
    for label in cfg:
      for successor in cfg[label]:
        if successor in predecessors:
          predecessors[successor].append(label)
        else:
          predecessors[successor] = [label]
    return predecessors

def getSuccessors(block, cfg):
    if block not in cfg:
      return []
    return cfg[block]

def getPredecessors(block, predecessors):
    if block not in predecessors:
        return []
    return predecessors[block]