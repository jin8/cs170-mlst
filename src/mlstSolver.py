import sys, fileinput, input, input.Graph

def mlstSolver(graph):
	forest = []
	S, d = {}, {}

	for v in graph.getVertices():
		S[v] = Graph(None)
		S[v].addVertex(v)
		d[v] = 0

	for v in graph.getVertices():
