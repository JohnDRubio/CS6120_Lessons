import sys
import json
import itertools
sys.path.append("../library")
sys.path.append("../lesson05")
import cfg
# import graph
import dominators
from stack import Stack

def getAllVars(insns):
    vars = set()
    for insn in insns:
        if 'dest' in insn:
            vars.add(insn['dest'])
    return vars

def getDefBlocks(insns):
    defs = {}   # map from varName to set of blocks where var is def'd
    basicBlocks = cfg.formBasicBlocks(insns)
    for block in basicBlocks:
        blockName = block[0]['label']
        for insn in block:
            if 'dest' in insn:
                if insn['dest'] not in defs:
                    defs[insn['dest']] = set()
                    defs[insn['dest']].add(blockName)
                else:
                    defs[insn['dest']].add(blockName)
    return defs

def getBlock(block):
    for b in blocks:
         if b[0]['label'] == block:
             return b

def addPhiNode(var,block):
    preds = predecessors[block]
    phiNode = {'args': [var]*len(preds), 'dest': var, 'labels': preds, 'op': 'phi', 'type': 'int'} # don't hardcode int type
    b = getBlock(block)
    b.insert(1,phiNode)

def usesVar(block,var):
    b = getBlock(block)
    for insn in b:
        if 'args' in insn:
            if var in insn['args']:
                return True
    return False

def insertPhiNodes():
    phis = {} # l0: [a,b,c] , l1: [a] , ...
    for v in vars:
        for d in defs[v]:
            if d in domFrontier:
                for block in domFrontier[d]:
                    if usesVar(block,v):
                        if block not in phis:
                            phis[block] = set()
                            phis[block].add(v)
                            addPhiNode(v,block)
                        else:
                            if v not in phis[block]:
                                phis[block].add(v)
                                addPhiNode(v,block)

def rename(block):
    label = block[0]['label']
    pops = {}    # map from varName -> number of pops

    for insn in block:
        if 'args' in insn and insn['op'] != 'phi':
            args = insn['args']
            newArgs = []
            for arg in args:
                newArgs.append(stack[arg].peek())
            insn['args'] = newArgs

        if 'dest' in insn:
            dest = insn['dest']     
            newDestName = dest+'.'+str(newNames[dest])
            insn['dest'] = newDestName

            if dest in pops:
                pops[dest] += 1
            else:
                pops[dest] = 1 
            
            newNames[dest] = newNames[dest]+1
            stack[dest].push(newDestName)

    successors = c[label]
    for succ in successors:
        succBlock = getBlock(succ)
        for insn in succBlock:
            if 'op' in insn:
                if insn['op'] == 'phi':
                    labelIndex = -1
                    for i, succLabel in enumerate(insn['labels']):
                        if succLabel == label:
                            labelIndex = i
                    if 'args' in insn:
                        for i in range(len(insn['args'])):
                            if i == labelIndex:
                                insn['args'][i] = stack[insn['args'][i]].peek()
    
    if label in domTree:
        immediatelyDominated = domTree[label]
        for b in immediatelyDominated:
            rename(getBlock(b))

    for dest in pops:
        while pops[dest] != 0:
            stack[dest].pop()
            pops[dest] -= 1

def fromSSA():
    numSSA = 0
    for block in blocks:
        currentLabel = block[0]['label']
        for insn in block:
            if 'op' in insn:
                if insn['op'] == 'phi':
                    args = insn['args']
                    labels = insn['labels']
                    for i,label in enumerate(labels):
                        addNewBlock(insn['dest'],args[i],insn['type'],currentLabel,numSSA)
                        addPredsToNewBlock(label,numSSA,currentLabel)
                        numSSA = numSSA + 1
                    block.remove(insn)
                        

def addPredsToNewBlock(predLabel, currentNum, oldLabel):
    toLabel = 'ssaLabel_'+str(currentNum)
    blockPhiNode = getBlock(predLabel)
    lastInsn = blockPhiNode[-1]
    if lastInsn['op'] == 'jmp' and lastInsn['labels'][0] == oldLabel: # second check may not be necessary
        lastInsn['labels'][0] = toLabel
    elif lastInsn['op'] == 'br' and oldLabel in lastInsn['labels']:
        if lastInsn['labels'][0] == oldLabel:
            lastInsn['labels'][0] = toLabel
        else:
            lastInsn['labels'][1] = toLabel
    else:
        blockPhiNode.append({"labels": [toLabel], "op": "jmp"})

def addNewBlock(destVar,idVar,type,labelTo,num):
    blockLabel = 'ssaLabel_'+str(num)
    labelInsn = {"label": blockLabel}
    idInsn = {'dest': destVar, 'args': [idVar], 'op': 'id', 'type': type}
    jmpInsn = {"labels": [labelTo], "op": "jmp"}
    newBlock = []
    newBlock.append(labelInsn)
    newBlock.append(idInsn)
    newBlock.append(jmpInsn)
    blocks.append(newBlock)


def toSSA():
    insertPhiNodes()
    rename(blocks[0])

program = json.load(sys.stdin)
# file = open('C:\\Users\\rubio\\Documents\\personal\\School\\CS6120\\lessons\\CS6120_Lessons\\lesson06\\test.json')
# program = json.load(file)
for func in program['functions']:
    stack = {}                                                          # stack[v] stack of names for var v
    newNames = {}                                                       # {x:1,y:1,z:2,a:5} means that the next var for x is x1, z is z5, etc.
    vars = getAllVars(func['instrs'])                                   # set of all variables in func
    for v in vars:
        stack[v] = Stack()
        stack[v].push(v+'.')
        newNames[v] = 1

    c = cfg.createCFG(func['instrs'])
    blocks = cfg.formBasicBlocks(func['instrs'])
    predecessors = cfg.buildPredecessorList(c)
    doms = dominators.getDominators(c, predecessors)

    defs = getDefBlocks(func['instrs'])                                 # map from varName -> set of blocks where varName is defined
    domFrontier = dominators.getDominanceFrontier(doms, predecessors)   # map from block, b, -> set of blocks in b's dominance frontier
    domTree = dominators.getDominatorTree(doms)
    toSSA()
    fromSSA()
    func['instrs'] = list(itertools.chain(*blocks))
    #graph.createGraph(c,func['name']+"CFG")
    #graph.createGraph(dominators.getDominatorTree(doms),func['name']+"DomTree")

json.dump(program, sys.stdout, indent=2, sort_keys=True)