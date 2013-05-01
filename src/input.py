import fileinput, sys

print sys.argv[1]
print sys.argv[2]


class Graph:
    def __init__(self, inputFile):
        if inputFile == None: return
        self.graph, self.numEdges = {}, int(inputFile.readline().strip())
        for i in range(0, self.numEdges):
            edge = inputFile.readline().split(' ')
            vertex1, vertex2 = edge[0].strip(), edge[1].strip()
            if not vertex1 in self.graph: self.graph[vertex1] = []
            if not vertex2 in self.graph: self.graph[vertex2] = []
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
    
    def deleteEdge(self):
        return None
    
    def getEdges(self):
        g, edges = self.graph, []
        for u in g.keys():
            for v in g[u]:
                g[v].remove(u)
                edges.append([u, v])
        return edges
                
    def outputGraph(self, outputFile):
        edges = self.getEdges()
        outputFile.write(str(self.numEdges) + "\n")
        for edge in edges:
            outputFile.write(min(edge[0], edge[1]) + " " + max(edge[0], edge[1]) + "\n")

def createGraphs(graphs):
    f = open(sys.argv[1])
    numGraphs = int(f.readline())
    for i in range(0, numGraphs):
        graphs.append(Graph(f))
    outputGraphs(graphs)
    f.close()
    
def outputGraphs(graphs):
    f = open(sys.argv[2], 'w')
    f.write(str(len(graphs)) + "\n")
    for graph in graphs:
        graph.outputGraph(f)
    f.close()
          
graphs = []
createGraphs(graphs)         

