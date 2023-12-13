def formBasicBlocks(insns, funcName=None):
    basicBlocks = []
    currBlock = []
    for i in insns:
        if 'label' in i:
            basicBlocks.append(currBlock)
            currBlock = []
            currBlock.append(i)
        elif i['op'] == 'br' or i['op'] == 'jmp' or i['op'] == 'ret':
            currBlock.append(i)
            basicBlocks.append(currBlock)
            currBlock = []
        else:
            currBlock.append(i)
    basicBlocks.append(currBlock)
    basicBlocks = removeEmptyBasicBlocks(basicBlocks)
    basicBlocks = addLabels(basicBlocks, funcName)
    return basicBlocks

def addLabels(basicBlocks, funcName=None):
    num = 0
    for i, block in enumerate(basicBlocks):
        if i == 0 and funcName is not None:
            block.insert(0,{"label": funcName})
        elif 'label' not in block[0]:
            block.insert(0,{"label": "label_"+str(num)})
            num = num + 1
    return basicBlocks

def removeEmptyBasicBlocks(basicBlocks):
    newBasicBlocks = [x for x in basicBlocks if x != []]
    return newBasicBlocks

def dfs(visited, graph, node, nodes):
    if node not in visited:
        nodes.add(node)
        visited.add(node)
        if node in graph:
            for child in graph[node]:
                dfs(visited,graph,child,nodes)
    return nodes

def getNumNodes(graph):
    if len(list(graph.keys())) == 0:    # This is a hack - single-node CFGs don't have dom trees
        return 1                        # since we're assuming immediate dominance isn't reflexive.
                                        # Therefore, we want to return 1 for empty domTree graphs so
                                        # it matches the number of nodes in single-node CFGs 
    start = list(graph.keys())[0]       
    visited = set()                     
    nodes = set()
    throwAway = dfs(visited, graph, start, nodes)
    return len(visited)

def pruneCFG(cfg):
    start = list(cfg.keys())[0]
    reachableNodes = dfs(set(),cfg,start, set())

    for node in cfg.copy():
        if node not in reachableNodes:
            del cfg[node]

def createCFG(insns):
    basicBlocks = formBasicBlocks(insns)
    cfg = {}
    for i,block in enumerate(basicBlocks):
        label = block[0]['label']
        lastInstr = block[-1]
        if 'label' in lastInstr:
            if i < len(basicBlocks) - 1:
                cfg[label] = [basicBlocks[i+1][0]['label']]
            else:
                cfg[label] = []
        elif lastInstr['op'] == 'br' or lastInstr['op'] == 'jmp':
            cfg[label] = lastInstr['labels']
        else:
            if i < len(basicBlocks) - 1 and lastInstr['op'] != 'ret':
                cfg[label] = [basicBlocks[i+1][0]['label']]
            else:
                cfg[label] = []

    # pruneCFG removes nodes from CFG that
    # are unreachable from entry
    #
    #   Ex/
    #       label_0:        
    #           x: int = const 5
    #           ret x
    #       label_1:        // assume there is no jmp to label_1
    #           jmp end     // so label_1 is an unreachable basic block  
          
    pruneCFG(cfg)
    return cfg

def buildPredecessorList(cfg):
    predecessors = {}
    for label in cfg:
      for successor in cfg[label]:
        if successor in predecessors:
          predecessors[successor].append(label)
        else:
          predecessors[successor] = [label]
    return predecessors

def getSuccessors(block, cfg):
    if block not in cfg:
      return []
    return cfg[block]

def getPredecessors(block, predecessors):
    if block not in predecessors:
        return []
    return predecessors[block]