#graph =  {0:[1,10],1:[4,10],4:[1],10:[0,1]}
def findMaxLeafTree(graph):
    newGraph = {}
    numEdgeForEachVertex = {}
    vertices =[k for k,v in graph.items()]

    for x in vertices:
        if len(graph[x]) not in numEdgeForEachVertex:
            numEdgeForEachVertex[len(graph[x])]= list()           
        numEdgeForEachVertex[len(graph[x])].append(x)

    while vertices:
        edges = numEdgeForEachVertex.keys()
        maxEdge = max(edges)
        for x in numEdgeForEachVertex[maxEdge]:
            for y in graph[x]:
                if y in vertices:
                    if x not in newGraph:
                        newGraph[x] = list()
                    if y not in newGraph[x]:
                        newGraph[x].append(y)             
                    if y not in newGraph:
                        newGraph[y] = list()
                    if x not in newGraph[y]:
                        newGraph[y].append(x)
                    if y in vertices:
                        vertices.remove(y)
                if x in vertices:
                    vertices.remove(x)
        del numEdgeForEachVertex[maxEdge]
    return newGraph



