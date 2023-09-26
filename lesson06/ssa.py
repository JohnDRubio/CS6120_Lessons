import sys
import json
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

def addPhiNode(var,block,blocks,predsList):
    preds = predsList[block]
    phiNode = {"args": [var]*len(preds), "dest": var, "labels": preds, "op": "phi", "type": "int"}
    for b in blocks:
        if b[0]['label'] == block:
            blocks.insert(1,phiNode)

def insertPhiNodes(vars,defs,df,blocks,preds):
    phis = {} # l0: [a,b,c] , l1: [a] , ...
    for v in vars:
        for d in defs[v]:
            for block in df[d]:
                if block in defs[v]:
                    if block not in phis:
                        phis[block] = set()
                        phis[block].add(v)
                        addPhiNode(v,block,blocks,preds)
                    else:
                        if v not in phis[block]:
                            phis[block].add(v)
                            addPhiNode(v,block,blocks,preds)

def main():
    program = json.load(sys.stdin)
    for func in program['functions']:
        print(func['name']+' function\n')

        c = cfg.createCFG(func['instrs'])
        blocks = cfg.formBasicBlocks(func['instrs'])
        predecessors = cfg.buildPredecessorList(c)
        doms = dominators.getDominators(c, predecessors)

        #vars = getAllVars(func['instrs'])                               # set of all variables in func
        # print(str(vars))
        #defs = getDefBlocks(func['instrs'])                        # map from varName -> set of blocks where varName is defined
        # print(str(defBlocks))
        #domFrontier = dominators.getDominanceFrontier(doms, predecessors)   # map from block, b, -> set of blocks in b's dominance frontier
        # print(str(domFrontier))
        #domTree = dominators.getDominatorTree(doms)                         # map from block, b, -> set blocks that b immediately dominates
        # print(str(domTree))

        #graph.createGraph(c,func['name']+"CFG")
        #graph.createGraph(dominators.getDominatorTree(doms),func['name']+"DomTree")

if __name__ == "__main__":
    main()