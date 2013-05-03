import fileinput, sys

class Graph:
    def __init__(self, inputFile):
        self.graph = {}
        if inputFile == None:
            self.numEdges = 0
            return
        self.numEdges = int(inputFile.readline().strip())
        for i in range(0, self.numEdges):
            edge = inputFile.readline().split(' ')
            vertex1, vertex2 = int(edge[0].strip()), int(edge[1].strip())
            if not vertex1 in self.graph.keys(): self.graph[vertex1] = []
            if not vertex2 in self.graph.keys(): self.graph[vertex2] = []
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
    
    def deleteEdge(self, edge):
        u, v = edge
        self.graph[u].remove(v)
        self.graph[v].remove(u)
        self.numEdges -= 1
    
    def addEdge(self, edge):
        u, v = edge
        try:
            self.graph[u].append(v)
        except Exception:
            self.graph[u] = []
            self.graph[u].append(v)
        try:
            self.graph[v].append(u)
        except Exception:
            self.graph[v] = []
            self.graph[v].append(u)
        self.numEdges += 1
    
    def getEdges(self):
        g, edges = self.graph, []
        for u in g.keys():
            for v in g[u]:
                g[v].remove(u)
                edges.append([min(u, v), max(u, v)])
        return edges
    
    def getVertices(self):
        return self.graph.keys()
        
    def getAdjacentVertices(self, vertex):
        return self.graph[vertex]

    def addVertex(self, vertex):
        self.graph[vertex] = []

    def mergeGraphs(self, graph):
        edges = self.getEdges()
        newEdges = graph.getEdges()
        for edge in newEdges:
            if not edge in edges:
                self.addEdge(edge)
                
    def outputGraph(self, outputFile):
        edges = self.getEdges()
        outputFile.write(str(self.numEdges) + "\n")
        for edge in edges:
            outputFile.write(str(min(edge[0], edge[1])) + " " + str(max(edge[0], edge[1])) + "\n")

def createGraphs(graphs, inputFileName):
    f = open(inputFileName)
    numGraphs = int(f.readline())
    for i in range(0, numGraphs):
        graphs.append(Graph(f))
    f.close()
    
def outputGraphs(graphs, outputFileName):
    f = open(outputFileName, 'w')
    f.write(str(len(graphs)) + "\n")
    for graph in graphs:
        graph.outputGraph(f)
    f.close()

import mlstSolver
graphs, outputs = [], []
createGraphs(graphs, sys.argv[1]) 
for i in range(0, len(graphs)):
    outputs.append([])
    mlstSolver.mlstSolver(graphs[i], outputs[i])

outputGraphs(outputs, sys.argv[2])

