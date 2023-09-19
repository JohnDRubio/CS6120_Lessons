import cfg
import sys
import json

'''
    input: CFG

    output: map: label -> set of labels
            where label represents a node
            and set of labels are the nodes
            that dominate the label
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
        print(str(getDominatorTree(doms)))

if __name__ == "__main__":
    main()