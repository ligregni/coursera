# Desing and analysis of algorithms - Part 2
# Week 3

import sys

class Item:
    def __init__(self, v, w):
        self.value = v
        self.weight = w

def solve(n, w, m, items):
    if n <= 0 or w <= 0:
        return 0
    if (n,w) not in m:
        m[(n,w)] = max(solve(n-1,w,m,items), (solve(n-1,w-items[n-1].weight,m,items) + items[n-1].value) if items[n-1].weight <= w else 0)
    return m[(n,w)]
        
W,n = map(int, raw_input().split())
sys.setrecursionlimit(max(W,n)+1)
items = list()
m = dict()

for i in xrange(n):
    v,w = map(int, raw_input().split())
    items.append(Item(v,w))

print solve(n, W, m, items)
