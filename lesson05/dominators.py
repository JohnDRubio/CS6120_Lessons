import cfg
import sys
import json

'''
    input: CFG

    output: map: label -> set of labels
            where label represents some node
            in CFG, A, and set of labels are the nodes
            that dominate A
'''
def getDominators(c, predecessors):
    dom = {}        # map from label to set
    changing = True

    while changing:
        prevDom = dom.copy()
        for vertex in c:
            dominatorsOfPredecessors = []   # list of sets
            for predecessor in cfg.getPredecessors(vertex,predecessors):
                dominatorsOfPredecessors.append(dom[predecessor])
            intersection = set.intersection(*dominatorsOfPredecessors) if dominatorsOfPredecessors else set()
            intersection.add(vertex)
            dom[vertex] = intersection.copy()
            changing = prevDom == dom
    return dom

def doesStrictlyDominate(A, B, dom):
    return A in dom[B] and A != B

def doesImmediatelyDominate(A, B, dom):
    if A not in dom[B]:
        return False
    
    strictlyDominatesB = set()
    for vertex in dom:
        if doesStrictlyDominate(vertex, B, dom):
            strictlyDominatesB.add(vertex)

    for vertex in strictlyDominatesB:
        if doesStrictlyDominate(A, vertex, dom):
            return False

    return True

def getDominatorTree(dom):
    domTree = {}
    for vertex in dom:
        for dominator in dom[vertex]:
            if doesImmediatelyDominate(dominator,vertex,dom):
                if dominator not in domTree:
                    domTree[dominator] = set()
                domTree[dominator].add(vertex)
    return domTree

def inDominanceFrontier(A, B, dom, predecessors):
    if doesStrictlyDominate(A,B,dom) or A == B:
        return False  
    preds = cfg.getPredecessors(B, predecessors)

    # Here, we ran into a weird situation where: 
    #     A is a pred of B 
    #     A does not dominate B 
    #     BUT A dominates itself therefore B is in the dom frontier of A
    for pred in preds:
        if A in dom[pred]: 
            return True
    return False

def getDominanceFrontier(dom,predecessors):
    domFrontier = {}
    for A in dom:
        for B in dom:
            if inDominanceFrontier(A,B,dom,predecessors):
                if A not in domFrontier:
                    domFrontier[A] = set()
                domFrontier[A].add(B)
    return domFrontier 

def main():
    program = json.load(sys.stdin)
    # data = open('C:\\Users\\rubio\\Documents\\personal\\School\\CS6120\\lessons\\CS6120_Lessons\\lesson04\\reaching_def_test2.json')
    # program = json.load(data)
    for func in program['functions']:
        c = cfg.createCFG(func['instrs'])
        predecessors = cfg.buildPredecessorList(c)
        doms = getDominators(c, predecessors)
        # print(str(doms))
        # print(doesStrictlyDominate('label_0', 'label_0', doms))
        # print(doesImmediatelyDominate('label_0', 'l4', doms))
        # print(str(getDominatorTree(doms)))
        print(str(getDominanceFrontier(doms, predecessors)))
        # print(inDominanceFrontier('l3','l3',doms, predecessors))

if __name__ == "__main__":
    main()