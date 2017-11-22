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

    def bfs(self, s):
        visited = [False] * len(self.graph)

        queue = [s]
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s)
            print(s)
            for i in self.graph[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.bfs(2)
