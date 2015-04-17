import sys
sys.path.insert(0, '../lib')

from library import Set

class Edge:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.cost = c

n = int(raw_input())
edges = []

for line in sys.stdin:
    if len(line) > 1:
        a,b,c = map(int, line.split())
        edges.append(Edge(a,b,c))

edges.sort(key=lambda x: x.cost)
s = Set(n+1)
clusters = n
k = 4
solved = False
answer = 0

for edge in edges:
    if clusters <= k:
        solved = True
    #print edge.cost, edge.a, edge.b, s.find(edge.a), s.find(edge.b), clusters
    if not s.sameSet(edge.a, edge.b):
        if not solved:
            s.union(edge.a, edge.b)
            clusters -= 1
        else:
            answer = edge.cost
            break

print answer
