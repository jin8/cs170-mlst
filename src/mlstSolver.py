import sys, fileinput

#source: http://repository.cmu.edu/cgi/viewcontent.cgi?article=1417&context=tepper
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
        #print "v = " + str(v)
        #print "dict is" + str(S)
        #print "degree is" + str(d)
    
    for edge in forest:
        output.addEdge(edge)
    for v in graph.getVertices():
        if v not in output.getVertices():
            output.graph[v] = []
        
    edges = mergeSets(graph, output, findColoredSets(graph, output))
    for edge in edges:
        output.addEdge(edge)
    return output

        
def findColoredSets(graph, output):
    vertices, visited, color = graph.getVertices(),[], {}
    currentColor = 0
    while (len(vertices) != 0):
        start = [vertices[0]]
        color[currentColor] = []
        while len(start) != 0:
            node = start.pop(0)    
            if node not in visited:
                visited.append(node)
                start.extend(output.getAdjacentVertices(node))
                vertices.remove(node)
                color[currentColor].append(node)
        currentColor += 1
    return color
    
def mergeSets(graph, forestGraph, ColoredSets):
    edges, sets = [], ColoredSets.values()
    if len(sets) == 1: return []
    while len(sets) > 1:
        edge, leafEdges = None, []
        for v in sets[0]:
            for u in graph.getAdjacentVertices(v):
                if u in sets[0]: continue
                if len(forestGraph.getAdjacentVertices(v)) == 1 or len(forestGraph.getAdjacentVertices(u)) == 1:
                    leafEdges.append([u,v])
                    continue
                edge = [u, v]
                break
            if edge != None: break
        if edge == None:
            for e in leafEdges:
                if len(forestGraph.getAdjacentVertices(e[0])) > 1 or len(forestGraph.getAdjacentVertices(e[1])) > 1:
                    edge = e
                    break
        if edge == None: edge = leafEdges[0]
        edges.append(edge)
        index = -1
        for i in range(1, len(sets)):
            if sets[i] == None:
                print "blah"
            if edge[0] in sets[i] or edge[1] in sets[i]:
                index = i
                break
        s = sets[0] + sets[index]
        sets.remove(sets[index])
        sets.remove(sets[0])
        sets.append(s)
    return edges
        
            
            
                
                    
                    
                    
                    
                    