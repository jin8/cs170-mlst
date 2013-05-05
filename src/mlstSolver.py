import sys, fileinput

def solver(graph, output):
    forest = []
    S, d = {}, {}
    for v in graph.getVertices():
        S[v] = [v]
        d[v] = 0
      
    for v in graph.getVertices():
        S2 = []
        d2 =0
        
        for u in graph.getAdjacentVertices(v):
            if not u in S[v] and len(set(S[u])&set(S2)) == 0:
                d2 += 1
                S2.extend(S[u])
        if d[v]+d2 >= 3:
            for s in S2:
                forest.append([s,v])
                S[v] = list((set(S[v])|set(S[s])))
                S[s] = S[v]
                d[s] += 1
                d[v] += 1
    
    for edge in forest:
        output.addEdge(edge)
		

    return output

        
