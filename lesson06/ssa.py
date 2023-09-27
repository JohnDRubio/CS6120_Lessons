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
    phiNode = {'args': [var]*len(preds), 'dest': var, 'labels': preds, 'op': 'phi', 'type': 'int'}
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
    pops = set()

    for insn in block:
        if 'dest' in insn:
            # if insn['op'] != 'phi':
            if 'args' in insn:
                args = insn['args']
                newArgs = []
                for arg in args:
                    newArgs.append(stack[arg].peek())
                insn['args'] = newArgs

                for newArg in newArgs:
                    stack[newArg] = Stack()
                    stack[newArg].push(newArg)
                    numbers[newArg] = 1

                dest = insn['dest']
                newDestName = dest+str(numbers[dest])
                insn['dest'] = newDestName

                stack[newDestName] = Stack()
                stack[newDestName].push(newDestName)
                numbers[newDestName] = 1
                
                numbers[dest] = numbers[dest]+1
                stack[dest].push(newDestName)
                pops.add(dest)

    successors = c[label]
    for succ in successors:
        succBlock = getBlock(succ)
        for insn in succBlock:
            if 'op' in insn:
                if insn['op'] == 'phi':
                    if 'args' in insn:
                        args = insn['args']
                        newArgs = []
                        for arg in args:
                            newArgs.append(stack[arg].peek())
                        insn['args'] = newArgs
    
    if label in domTree:
        immediatelyDominated = domTree[label]
        for b in immediatelyDominated:
            rename(getBlock(b))
    
    for pop in pops:
        stack[pop].pop()

def toSSA():
    insertPhiNodes()
    rename(blocks[0])

program = json.load(sys.stdin)
# file = open('C:\\Users\\rubio\\Documents\\personal\\School\\CS6120\\lessons\\CS6120_Lessons\\lesson06\\test.json')
# program = json.load(file)
for func in program['functions']:
    stack = {} # stack[v] stack of names for var v
    numbers = {} # {x:1,y:1,z:2,a:5} means that the next var for x is x1, z is z5, etc.
    vars = getAllVars(func['instrs'])                                   # set of all variables in func
    for v in vars:
        stack[v] = Stack()
        stack[v].push(v)
        numbers[v] = 1

    c = cfg.createCFG(func['instrs'])
    blocks = cfg.formBasicBlocks(func['instrs'])
    predecessors = cfg.buildPredecessorList(c)
    doms = dominators.getDominators(c, predecessors)

    defs = getDefBlocks(func['instrs'])                                 # map from varName -> set of blocks where varName is defined
    domFrontier = dominators.getDominanceFrontier(doms, predecessors)   # map from block, b, -> set of blocks in b's dominance frontier
    domTree = dominators.getDominatorTree(doms)
    toSSA()
    func['instrs'] = list(itertools.chain(*blocks))
    #graph.createGraph(c,func['name']+"CFG")
    #graph.createGraph(dominators.getDominatorTree(doms),func['name']+"DomTree")

json.dump(program, sys.stdout, indent=2, sort_keys=True)