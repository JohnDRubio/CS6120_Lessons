import dominators
import json
import sys

def getPathsHelper(c, node, dest, path, visited, allPaths):
    path.append(node)
    visited.append(node)
    if node == dest:
        allPaths.append(path[:])
    
    else:
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

def confirmDominators(actualDoms, cfg, vertex):
    start = list(cfg.keys())[0]
    allPaths = []
    getPaths(cfg, start, vertex, allPaths)
    allPaths = convertToSets(allPaths)
    intersection = set.intersection(*allPaths)
    return intersection == actualDoms
    