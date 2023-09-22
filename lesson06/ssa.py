import cfg
import sys
import json
import graph
import dominators 

def main():
    program = json.load(sys.stdin)
    for func in program['functions']:
        print(func['name']+' function')
        c = cfg.createCFG(func['instrs'])
        predecessors = cfg.buildPredecessorList(c)
        doms = dominators.getDominators(c, predecessors)

        vars = cfg.getAllVars(func['instrs'])                               # set of all variables in func
        # print(str(vars))
        defBlocks = cfg.getDefBlocks(func['instrs'])                        # map from varName -> set of blocks where varName is defined
        # print(str(defBlocks))
        successors = cfg.buildSuccessorList(c)                              # map from block, b, -> set of of b's successor blocks
        # print(str(successors))
        domFrontier = dominators.getDominanceFrontier(doms, predecessors)   # map from block, b, -> set of blocks in b's dominance frontier
        # print(str(domFrontier))
        domTree = dominators.getDominatorTree(doms)                         # map from block, b, -> set blocks that b immediately dominates
        # print(str(domTree))

        graph.createGraph(c,func['name']+"CFG")
        graph.createGraph(dominators.getDominatorTree(doms),func['name']+"DomTree")

if __name__ == "__main__":
    main()