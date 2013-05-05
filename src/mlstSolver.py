import sys, fileinput

def solver(graph, output):
	forest = []
	S, d = {}, {}
        if graph.numEdges <= 2:
            for v in graph.getVertices():
                for u in graph.getAdjacentVertices(v):
                        if not v in S or not u in S:
                                S[v]= [u]
                                forest.append([u,v])
                  
        else:
                                
                for v in graph.getVertices():
                        S[v] = [v]
                        d[v] = 0

                for v in graph.getVertices():
                        S2 = []
                        d2 =0

                        for u in graph.getAdjacentVertices(v):
                                if not u in S[v] and not S[u] in S2:
                                        d2 += 1
                                        S2.append(S[u])
                        if d[v]+d2 >= 3:
                                for s in S2:
                                        forest.append([s[0],v])
                                        S[v] = list(set(S[v]).union(S[s[0]]))
                                        S[s[0]] = S[v]
                                        d[s[0]] += 1
                                        d[v] += 1
        for edge in forest:
                output.addEdge(edge)
		

	return output

        
