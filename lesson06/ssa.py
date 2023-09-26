import sys
import json
import itertools
sys.path.append("../library")
sys.path.append("../lesson05")
import cfg
import graph
import dominators

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
    phiNode = {"args": [var]*len(preds), "dest": var, "labels": preds, "op": "phi", "type": "int"}
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
    stack = {} # stack[v] stack of names for var v

    for insn in block:
        pass

def toSSA():
    insertPhiNodes()
    #rename(blocks[0])

program = json.load(sys.stdin)
for func in program['functions']:
    c = cfg.createCFG(func['instrs'])
    blocks = cfg.formBasicBlocks(func['instrs'])
    predecessors = cfg.buildPredecessorList(c)
    doms = dominators.getDominators(c, predecessors)

    vars = getAllVars(func['instrs'])                               # set of all variables in func
    defs = getDefBlocks(func['instrs'])                       # map from varName -> set of blocks where varName is defined
    domFrontier = dominators.getDominanceFrontier(doms, predecessors)   # map from block, b, -> set of blocks in b's dominance frontier
    toSSA()
    func['instrs'] = list(itertools.chain(*blocks))
    #graph.createGraph(c,func['name']+"CFG")
    #graph.createGraph(dominators.getDominatorTree(doms),func['name']+"DomTree")

json.dump(program, sys.stdout, indent=2, sort_keys=True)