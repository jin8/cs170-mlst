import sys, fileinput

def mlstSolver(graph, output):
	forest = []
	S, d = {}, {}

	for v in graph.getVertices():
		S[v] = [v]
		d[v] = 0

	for v in graph.getVertices():
		S2, d2 = [], 0
		for u in graph.getAdjacentVertices(v):
			if not u in S[v] and len(list(set(S[u]).intersection(S2)))==0:
				d2 += 1
				S2.append([S[u]])
		if d[v]+d2 >= 3:
			for s in S2:
				forest.append([u,v])
				S[v] = list(set(S[v]).union(S[u]))
				S[u] = S[v]
				d[u] += 1
				d[v] += 1
	for edge in forest:
		output.addEdge(edge)

	return output
