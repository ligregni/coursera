# Design and Analysis of Algorithms II
# Week 5
# Traveling Salesman Problem
# Bottom up approach

import math
import sys

def distance(a,b):
    return math.sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 )

def constructsets(m, n, i):
    if m == 0:
        return [0]
    r = []
    r += map(lambda x : x | i, constructsets(m-1, n-1, i*2))
    if m < n:
        r += constructsets(m, n-1, i*2)
    return r

def getsets(m, n):
    r = constructsets(m-1, n-1, 1)
    return r

def getelem(s, exclude=None):
    if exclude and exclude != 0:
        s = remove_from_set(s, exclude)
    r = []
    if exclude != 0:
        r.append(0)
    i = 1
    while s:
        if s & 0x1:
            r.append(i)
        i += 1
        s >>= 1
    return r

def remove_from_set(s, j):
    return s & ~(1 << (j-1))

n = int(raw_input())
mapa = list()
for i in xrange(n):
    mapa.append(tuple(map(float, raw_input().split())))

A = [ [ sys.maxint ] * n for i in range(2**(n-1)) ]

A[1][0] = 0

for m in xrange(2,n+1):
    print 'm', m
    for s in getsets(m, n):
        for j in getelem(s, 0):
            for k in getelem(s, j):
                if k == 0:
                    A[s][j] = min(A[s][j], A[s][k] + distance(mapa[j], mapa[k]))
                else:
                    A[s][j] = min(A[s][j], A[remove_from_set(s,j)][k] + distance(mapa[j], mapa[k]))

r = sys.maxint

for j in xrange(1,n):
    r = min(r, A[getsets(n, n)[0]][j] + distance(mapa[j], mapa[0]))

print int(r)
