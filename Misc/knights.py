#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


class Graph(object):
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
        from start.
        """
        visited = defaultdict(lambda: False)

        queue = [start]
        visited[start] = True

        depth = {}
        depth[start] = 0

        while queue:
            s = queue.pop(0)
            d = depth[s]
            if s == target:
                return d
            for i in self.graph[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    depth[i] = d + 1
        return -1


if __name__ == "__main__":
    g = Graph()
    g.add_edge('a', 1)
    g.add_edge('a', 2)
    g.add_edge(1, 2)
    g.add_edge(2, 'a')
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print(g.bfs(1, 'a'))
