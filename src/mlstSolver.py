import sys, fileinput

def solver(graph, output):
    forest = []
    S, d = {}, {}
    for v in graph.getVertices():
        S[v] = [v]
        d[v] = 0
      
    for v in graph.getVertices():
        S2 = {}
        d2 = 0
        for u in graph.getAdjacentVertices(v):
            if not u in S[v] and len(set(S[u])&set(S2)) == 0:
                d2 += 1
                S2[u] = S[u]
                
        if d[v]+d2 >= 3:
            setv = S[v]
            for u in S2.keys():
                forest.append([u,v])
                S[v] = list((set(S[v])|set(S[u])))
                #S[u] = list((set(S[v])|set(S[u]))) #S[u] = S[v] | S[u]
                d[u], d[v] = d[u] + 1, d[v] + 1
            for n in S[v]:
                S[n] = S[v]
        print "v = " + str(v)
        print "dict is" + str(S)
        print "degree is" + str(d)
    
    for edge in forest:
        output.addEdge(edge)    
    return output

        
def breadthFirstSearch(graph):
    vertices, visited, color = graph.getVertices(),[], []
    currentColor = 0
    while (len(vertices) != 0):
        start = [vertices[0]]
        while not len(start) != 0:
            node = start.pop(0)    
            if node not in visited:
                visited.append(node)
                start.extend(graph.getAdjacentVertices(node))
                vertices.remove(node)
                color[node] = currentColor
        currentColor++