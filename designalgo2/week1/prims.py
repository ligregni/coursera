# Prim's MST algorithm

import sys
sys.path.insert(0, '../lib')

from library import MinHeap

def solve1(n,m,graph):
    print 'Solve1'
    h = MinHeap()
    x = set()
    t = 0
    x.add(1)
    for edge,cost in graph[1]:
        h.insert(cost, (1,edge))
    while len(x) != n:
        cost,edge = None,None
        while True:
            cost,edge = h.top()
            h.delete(edge)
            if edge[1] not in x:
                break
        t += cost
        vertex = edge[1]
        x.add(vertex)
        for edge,cost in graph[vertex]:
            h.insert(cost,(vertex,edge))
    return t

def solve2(n,m,graph):
    print 'Solve2'
    h = MinHeap()
    x = set()
    t = 0
    for i in xrange(1,n+1):
        h.insert(sys.maxint, i)
    x.add(1)
    h.delete(1)
    for edge,cost in graph[1]:
        h.increase(edge, cost)
    while len(x) != n:
        cost,vertex = h.top()
        h.delete(vertex)
        x.add(vertex)
        t += cost
        for edge,cost in graph[vertex]:
            if edge not in x:
                h.increase(edge,cost)
    return t
    
n,m = map(int, raw_input().split())
graph = [ [] for i in range(n+1) ]

for i in xrange(m):
    a,b,c = map(int, raw_input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

print solve1(n,m,graph)
print solve2(n,m,graph)
