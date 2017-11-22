#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, v, w):
        self.graph[v].append(w)

    def add_undirected_edge(self, v, w):
        self.add_edge(v, w)
        self.add_edge(w, v)

    def bfs(self, start, target):
        visited = [False] * len(self.graph)

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
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print(g.bfs(1, 0))
