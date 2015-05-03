# Design and Analysis of Algorithms II
# Week 5
# Traveling Salesman Problem

import math
import sys

def distance(a,b):
    return math.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 )

def dp(m, mapa, s, j):
    ss = tuple(sorted(list(s)))
    #print ss, j
    if len(s) == 1:
        return 0
    if len(s) == 2:
        return distance(mapa[ss[0]], mapa[ss[1]])
    if j == 0:
        return sys.maxint
    if (ss,j) not in m:
        r = sys.maxint
        for k in s:
            if k != j and k != 0:
                r = min(r, dp(m, mapa, s - set([j]), k) + distance(mapa[j], mapa[k]))
        m[(ss,j)] = r
    return m[(ss,j)]

def tsp(mapa):
    r = sys.maxint
    s = set(range(len(mapa)))
    m = dict()
    for j in xrange(1, len(mapa)):
        r = min(r, dp(m, mapa, s,j) + distance(mapa[j], mapa[0]))
    print m
    return r

n = int(raw_input())
mapa = list()
for i in xrange(n):
    mapa.append(tuple(map(float, raw_input().split())))

print int(tsp(mapa))
