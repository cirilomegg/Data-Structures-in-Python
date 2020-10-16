class Edge:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


class Graph:
    def __init__(self, edges):
        self.dict = {}

        for current in edges:
            if not current.source in self.dict:
                self.dict[current.source] = []

            if not current.destination in self.dict[current.source]:
                self.dict[current.source].append(current.destination)

            if not current.destination in self.dict:
                self.dict[current.destination] = []

            if not current.source in self.dict[current.destination]:
                self.dict[current.destination].append(current.source)

    def print(self):
        for src in self.dict:
            for dest in self.dict[src]:
                print(f"({src} -> {dest}) ", end="")
            print()


if __name__ == "__main__":
    edges = [Edge(0, 1), Edge(1, 2), Edge(2, 0), Edge(2, 1),
             Edge(3, 2), Edge(4, 5), Edge(5, 4)]

    graph = Graph(edges)
    graph.print()
