from aoc import get_input, submit
from collections import defaultdict

def parse_graph(input):
    graph = defaultdict(set)
    for line in input.splitlines():
        a, b = line.split('-')
        graph[a].add(b)
        graph[b].add(a)
    return graph

def find_triangles(graph):
    result = set()
    for a in graph.keys():
        if a.startswith('t'):
            for b in graph[a]:
                for c in graph[a] & graph[b]:
                    result.add(','.join(sorted([a, b, c])))
    return result

# Bron–Kerbosch algorithm copied from wikipedia, whatever...
def find_cliques(graph):
    def recur(R, P, X):
        if not P and not X:
            return [','.join(sorted(R))]
        result = []
        for v in list(P):
            result.extend(recur(R + [v], P & graph[v], X & graph[v]))
            P.remove(v)
            X.add(v)
        return result
    return recur([], set(graph.keys()), set())

input = get_input(23)
graph = parse_graph(input)
submit(len(find_triangles(graph)))
submit(max(find_cliques(graph), key=len))
