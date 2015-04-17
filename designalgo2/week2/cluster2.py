import sys
sys.path.insert(0, '../lib')

from library import Set

class Vertex:
    def __init__(self, a):
        self.lista = a

class Edge:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.cost = c

def traverse(v, i, bits, edge, maxedge, leaves, a, b, s, f):
    if edge < 0:
        return
    if bits < 0:
        if leaves[a] is not None:
            s.union(i, leaves[a])
        elif edge == maxedge:
            leaves[a] = i
        return
    traverse(v, i, bits-1, edge if v.lista[bits] == 0 else edge-1, maxedge, leaves, a, (a+b)/2, s, 'LEFT')
    traverse(v, i, bits-1, edge if v.lista[bits] == 1 else edge-1, maxedge, leaves, (a+b)/2, b, s, 'RIGHT')

def get_sets(vertex, bits, max_edge_len):
    if len(vertex) == 0:
        return Set(0)
    leaves = [None for i in xrange(2**bits)]
    s = Set(len(vertex))
    for v in xrange(len(vertex)):
        if v % 10000 == 0:
            print 'processing vertex %i with %d clusters' % (v, s.getSetCount())
        traverse(vertex[v], v, bits-1, max_edge_len, max_edge_len, leaves, 0, len(leaves), s, 'ROOT')
    return s

n,bits = map(int, raw_input().split())
vertex = []

for i in xrange(n):
    line = raw_input()
    x = Vertex(tuple(map(int, line.split())))
    vertex.append(x)

clusters = get_sets(vertex, bits, 2).getSetCount()
print clusters
