free, IN, BN, LN, FL = [], [], [], [], []

def exactMlstSolver(graph, output):
    graphChanged = True
    while (graphChanged == True):
        graphChanged = reductionOne(graph) or reductionTwoAndThree(graph) or reductionFour(graph) or reductionFive(graph) or reductionSix(graph) or reductionSeven(graph)
    return graphChanged
            
def getDegree(vertex, graph):
    if vertex in BN:
        degree = len(set(graph.getAdjacentVertices(vertex) & (set(free)|set(FL))))
    elif vertex in free:
        degree = len(set(graph.getAdjacentVertices(vertex) & (set(free)|set(FL)|set(BN))))
    elif vertex in FL:
        degree = len(set(graph.getAdjacentVertices(vertex) & (set(free)|set(BN))))
    return degree

def reductionOne(graph):
    graphChanged = False
    for v in graph.getVertices():
        vInFL = v in FL
        vInBN = v in BN
        for u in graph.getAdjacentVertices(v):
            if vInFL and u in FL:
                graph.deleteEdge([u, v])
                graphChanged = True
            elif vInBN and u in BN:
                graph.deleteEdge([u, v])
                graphChanged = True
    return graphChanged

def reductionTwoAndThree(graph):
    graphChanged = False
    for v in graph.getVertices():
        degree = getDegree(v)
        if v in BN and getDegree(v, graph) == 0:
            BN.remove(v)
            LN.append(v)
            graphChanged = True
        elif v in free and getDegree(v, graph) == 1:
            free.remove(v)
            FL.append(v)
            graphChanged = True
    return graphChanged

def reductionFour(graph):
    graphChanged = False
    for v in graph.getVertices():
        if v in free and len(set(graph.getAdjacentVertices(v) & (set(free)|set(FL)))) == 0:
            free.remove(v)
            FL.append(v)
            graphChanged = True
    return graphChanged

def reductionFive(graph):
    graphChanged = False
    for x in graph.getVertices():
        if getDegree(x, graph) != 2 or x not in free: continue
        for y in graph.getAdjacentVertices(x):
            for z in graph.getAdjacentVertices(y):
                if x in graph.getAdjacentVertices(z):
                    free.remove(x)
                    FL.append(x)
                    graphChanged = True
    return graphChanged

def reductionSix(graph):
    graphChanged = False
    for v in graph.getVertices():
        if v in BN and isCutVertex(graph, v):
            BN.remove(v)
            IN.append(v)
            graphChanged = True
    return graphChanged
        
def isCutVertex(graph, vertex):
    start, visited = [], []
    g = graph.deepCopy()
    g.deleteVertex(vertex)
    start.append(g.getVertices()[0])
    while len(start) != 0:
        node = start.pop(0)    
        if node not in visited:
            visited.append(node)
            start.extend(g.getAdjacentVertices(node))
    if len(visited) != len(g.getVertices()): return True
    else: return False

def reductionSeven(graph):
    graphChanged = False
    for v in graph.getVertices():
        if v not in list(set(graph.getVertices()) - set(IN)): continue
        for u in graph.getAdjacentVertices(v):
            if u in LN:
                graph.deleteEdge([u, v])
                graphChanged = True
    return graphChanged
                
        