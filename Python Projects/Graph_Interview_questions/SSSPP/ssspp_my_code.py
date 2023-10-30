class Graph:
    def __init__(self, gdict) -> None:
        self.gdict = gdict
        self.path = []

    def bfs(self, start, end):
        visited = dict()
        queue = [start]
        visited[start] = True
        while queue:
            node = queue.pop(0)  # Pop the first element from the queue
            self.path.append(node)
            if node == end:
                break
            for neighbor in self.gdict[node]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.append(neighbor)

    def print_path(self):
        for i in range(len(self.path) - 1):
            print(self.path[i] + "->", end="")
        print(self.path[-1])


gdict = {"a": ["b", "c"], "b": ["a", "d", "g"], "c": ["a", "b"], "d": [
    "b", "c", "f"], "e": ["c", "f"], "f": ["e", "d", "g"], "g": ["b", "f"]}
g = Graph(gdict)
g.bfs("a", "f")
g.print_path()
