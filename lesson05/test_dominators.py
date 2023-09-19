def getPathsHelper(u, d, visited, path, cfg):
  visited[u] = True
  path.append(u)

  if u == d:
    print(path)
  else:
    for i in cfg[u]:
      if visited[i] == False:
        getPathsHelper(i,d,visited,path,cfg)
  
  path.pop()
  visited[u] = False


def getPaths(start, end,cfg):
  visited = {}
  for v in cfg:
    visited[v] = False
  return getPathsHelper(start, end, visited, [], cfg)


def confirmDominators(vertex,vertexDoms,cfg):
  # start = 0
  # getPaths(start,vertex,cfg)

  # pass