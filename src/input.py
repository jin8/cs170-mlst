import fileinput, sys

class Graph:
    def __init__(self, inputFile):
        if inputFile == None: return
        self.graph, self.numEdges = {}, int(inputFile.readline().strip())
        for i in range(0, self.numEdges):
            edge = inputFile.readline().split(' ')
            vertex1, vertex2 = int(edge[0].strip()), int(edge[1].strip())
            if not vertex1 in self.graph: self.graph[vertex1] = []
            if not vertex2 in self.graph: self.graph[vertex2] = []
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
                edges.append([u, v])
        return edges
    
    def getAdjacentVertices(self, vertex):
        return self.graph[vertex]
                
    def outputGraph(self, outputFile):
        edges = self.getEdges()
        outputFile.write(str(self.numEdges) + "\n")
        for edge in edges:
            outputFile.write(str(min(edge[0], edge[1])) + " " + str(max(edge[0], edge[1])) + "\n")

def createGraphs(graphs):
    f = open(sys.argv[1])
    numGraphs = int(f.readline())
    for i in range(0, numGraphs):
        graphs.append(Graph(f))
    graphs[1].addEdge([10, 4])
    graphs[1].deleteEdge([1,10])
    graphs[1].deleteEdge([10,4])
    outputGraphs(graphs[1:2])
    f.close()
    
def outputGraphs(graphs):
    f = open(sys.argv[2], 'w')
    f.write(str(len(graphs)) + "\n")
    for graph in graphs:
        graph.outputGraph(f)
    f.close()
          
graphs = []
createGraphs(graphs)         

