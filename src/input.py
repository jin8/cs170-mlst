import fileinput, sys

print sys.argv[1]
print sys.argv[2]


class Graph:
    def __init__(self, inputFile):
        if inputFile == None: return
        self.graph, self.numEdges = {}, int(inputFile.readline())
        for i in range(0, self.numEdges):
            edge = inputFile.readline().split(' ')
            vertex1, vertex2 = edge[0], edge[1]
            if not vertex1 in self.graph: self.graph[vertex1] = []
            if not vertex2 in self.graph: self.graph[vertex2] = []
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
    
    def deleteEdge(self):
        return None
                
    def outputGraph(self, outputFile):
        f = open(outputFile, 'w')
        f.writeLine()
        for i in range(0, self.graph.keys().size() - 1):
            f = 
            
graphs = []
def main():
    f = open(sys.argv[1])
    numGraphs = int(f.readline())
    for i in range(0, numGraphs):
        graphs.append(Graph(f))
    
         

