from collections import heapq


class Edge:

    def __init__(self, weight, start_vertex, target_vertex) -> None:
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Graph:

    def __init__(self, weight, start_vertex, target_vertex) -> None:

        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node:

    def __init__(self, name, visited, predecessor) -> None:
        self.name = name
        self.visited = visited
        self .predecessor = predecessor
        self.neighbour = []
        self.min_distance = float('inf')

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance

    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbour.append(edge)


class dijkstra:

    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.min_distance = 0

        heapq.heappush(self.heap, start_vertex)
# last 2.8.23
