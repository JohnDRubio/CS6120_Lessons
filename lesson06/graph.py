import graphviz

# {l0:[l1,l2], l2:[l3,4], ...}
def createGraph(dict, name):
  dot = graphviz.Digraph()

  for v1 in dict:
    dot.node(v1)
    for v2 in dict[v1]:
      dot.edge(v1,v2)
  
  dot.render('graphs/'+name+'.gv')