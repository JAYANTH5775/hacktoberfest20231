from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                print("enter the proper  Key value")
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    def bfs(self, vertex):

        visited = set()

        visited.add(vertex)

        queue = deque([vertex])

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            for adj_vertex in self.adjacency_list[current_vertex]:
                if adj_vertex not in visited:
                    visited.add(adj_vertex)
                    queue.append(adj_vertex)
# each vertexand the each edge is visitted oonce   time cmplexity is o(E+V)   space conmplexity is o(V)  (because of the visited set )

    def dfs(self, vertex):
        visited = set()
        stack = [vertex]

        while stack:
            cur_vertex = stack.pop()
            if cur_vertex not in visited:
                print(cur_vertex)
                visited.add(cur_vertex)
            for adj_vertex in self.adjacency_list[cur_vertex]:
                if adj_vertex not in visited:
                    stack.append(adj_vertex)


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")

my_graph.add_vertex("D")
my_graph.add_vertex("E")
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("B", "E")
my_graph.add_edge("D", "E")
my_graph.add_edge("C", "D")
my_graph.print_graph()


my_graph.bfs("A")

print("\n")
my_graph.dfs("A")
