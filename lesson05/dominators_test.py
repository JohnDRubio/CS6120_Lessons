import dominators
import json
import sys
import cfg

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

def main():
    program = json.load(sys.stdin)
    # data = open('C:\\Users\\rubio\\Documents\\personal\\School\\CS6120\\lessons\\CS6120_Lessons\\lesson04\\reaching_def_test2.json')
    # program = json.load(data)
    for func in program['functions']:
        c = cfg.createCFG(func['instrs'])
        start = 'label_0'       # this will likely be a constant
        end = 'end'             # this will change depending on which block we're interested in
        allPaths = []
        getPaths(c, start, end, allPaths)
        print(str(allPaths))

if __name__ == "__main__":
    main()