


from collections import defaultdict

class Graph: 
    def __init__(self, numberOfVertices) -> None:
        self.graph = defaultdict()
        self.numberOfVertices = numberOfVertices
    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)
    def topologicalSort()