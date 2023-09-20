import dominators
import json
import sys

def getPathsHelper(c, node, dest, path, visited, allPaths):
    path.append(node)
    visited.append(node)
    if node == dest:
        allPaths.append(path[:])
    
    else:
        if node in c:
            for n in c[node]:
                if n not in visited:
                    getPathsHelper(c,n,dest,path,visited,allPaths)
    path.pop()
    visited.pop()

def getPaths(c, start, dest, allPaths):
    path = []
    visited = []
    getPathsHelper(c,start,dest,path,visited,allPaths)

def convertToSets(allPaths):
    setList = []
    for l in allPaths:
        setList.append(set(l))
    return setList

def getDominators(cfg, vertex):
    start = list(cfg.keys())[0]
    allPaths = []
    getPaths(cfg, start, vertex, allPaths)
    allPaths = convertToSets(allPaths)
    intersection = set.intersection(*allPaths) if allPaths else set()
    # print("DOMINATORS EXPECTED\n\n")
    # print(intersection)
    return intersection 

def confirmDominators(ourDoms, cfg, vertex):
    return getDominators(cfg, vertex) == ourDoms

def confirmDomTree(ourDomTree, dominators):
    for vertex in ourDomTree:
        for child in ourDomTree[vertex]:
            for i in ourDomTree:
                if i != vertex and i != child:
                    if vertex in dominators[i] and dominators[child] == i:
                        return False
                    if vertex not in dominators[child]:
                        return False
    return True

def confirmDomFrontier(ourDomFrontier, dominators, predecessors, cfg):
    for A in cfg:
        if A in ourDomFrontier:
            for B in ourDomFrontier[A]:
                if A in dominators[B] and A != B:
                    return False
                numPredsDominated = 0
                for pred in predecessors[B]:
                    if A in dominators[pred]:
                        numPredsDominated = numPredsDominated + 1
                if numPredsDominated == 0:
                    return False
    return True