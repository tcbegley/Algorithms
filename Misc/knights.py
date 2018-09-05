from collections import defaultdict


class Graph:
    """
    Graph class. Add edges using add_edge or add_undirected_edge methods.
    Vertex labels can be any immutable type.
    """

    def __init__(self):
        """
        Graph is stored as a dictionary where vertex labels are the keys and
        the values are a list of labels of adjacent vertices.
        """
        self.graph = defaultdict(list)

    def add_edge(self, v, w):
        """
        Add a directed edge connecting vertex v to vertex w.
        """
        self.graph[v].append(w)

    def add_undirected_edge(self, v, w):
        """
        Add undirected edge connecting vertices v and w.
        """
        self.add_edge(v, w)
        self.add_edge(w, v)

    def bfs(self, start, target):
        """
        Conducts breadth first search for vertex target starting from vertex
        start. Returns length of shortest path, or -1 if target is unreachable
        from start, and optimal route. This function is just a wrapper that
        processes the returned dictionary.
        """
        depth, path_dict = self._bfs(start, target)
        best_path = []
        if path_dict:
            k = target
            best_path.append(k)
            while k != start:
                k = path_dict[k]
                best_path.append(k)
        return depth, best_path[::-1]

    def _bfs(self, start, target):
        """Implements the actual breadth first search."""
        visited = defaultdict(lambda: False)

        queue = [start]
        visited[start] = True

        depth = {}
        reached_from = {}
        depth[start] = 0

        while queue:
            s = queue.pop(0)
            d = depth[s]
            if s == target:
                return d, reached_from
            for i in self.graph[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    depth[i] = d + 1
                    reached_from[i] = s
        return -1, None


class Knight:
    """
    This class can be used to find the shortest path for a knight between two
    squares on a chessboard. It creates a graph where each vertex corresponds
    to a square on the chessboard and is connected to all other squares
    reachable in one move by the knight. The shortest path is then found by
    a breadth-first search on this graph.

    Graph vertices are indexed by 0, 1, ..., 63. self.vertex_map can be used to
    go between these numeric vertex labels and traditional chessboard labels,
    A1, C2 etc.
    """

    def __init__(self):
        self.board, self.vertex_map = generate_board()

    def shortest_path(self, start, stop):
        """Find shorest path between start and stop"""
        start_i = self.vertex_map.index(start)
        stop_i = self.vertex_map.index(stop)
        _, best_path = self.board.bfs(start_i, stop_i)
        return [self.vertex_map[i] for i in best_path]


def generate_board():
    """Generate graph of possible knight moves and lookup dictionary"""
    vertex_map = [b + a for b in "ABCDEFGH" for a in "12345678"]
    board = Graph()
    for i in range(8):
        for j in range(8):
            loc = 8 * i + j
            if i >= 2 and j > 0:
                # down 2, left 1
                board.add_edge(loc, loc - 17)
            if i >= 2 and j < 7:
                # down 2, right 1
                board.add_edge(loc, loc - 15)
            if i >= 1 and j > 1:
                # down 1, left 2
                board.add_edge(loc, loc - 10)
            if i >= 1 and j < 6:
                # down 1, right 2
                board.add_edge(loc, loc - 6)
            if i < 7 and j > 1:
                # up 1, left 2
                board.add_edge(loc, loc + 6)
            if i < 7 and j < 6:
                # up 1, right 2
                board.add_edge(loc, loc + 10)
            if i < 6 and j > 0:
                # up 2, left 1
                board.add_edge(loc, loc + 15)
            if i < 6 and j < 7:
                # up 2, right 1
                board.add_edge(loc, loc + 17)
    return board, vertex_map


if __name__ == "__main__":
    k = Knight()
    print(k.shortest_path("A1", "D4"))
