# Design and analysis of algorithms - Part II
# Week 4
# All Pairs Shortest Paths

from collections import defaultdict
import sys

n,m = map(int, raw_input().split())
edges = defaultdict(dict)

for i in xrange(m):
    u,v,c = map(int, raw_input().split())
    edges[u][v] = c

matrix = [ [ [ None ] * (2) for i in range(n+1) ] for i in range(n+1) ]

print 'finished reading', n, m

for i in xrange(1,n+1):
    for j in xrange(1,n+1):
        if i == j:
            matrix[i][j][0] = 0
        elif j in edges[i]:
            matrix[i][j][0] = edges[i][j]
        else:
            matrix[i][j][0] = sys.maxint

print 'finished initializing'

for k in xrange(1,n+1):
    if k % 10 == 0:
        print 'k = %d' % (k)
    for i in xrange(1, n+1):
        for j in xrange(1, n+1):
            matrix[i][j][k%2] = min(matrix[i][j][(k+1)%2], matrix[i][k][(k+1)%2] + matrix[k][j][(k+1)%2])

print 'finished floyd warshall'

# Check for negative length cycles
negative = False
for i in xrange(1,n+1):
    if matrix[i][i][n%2] < 0:
        negative = True
        break

print 'finished checking negative'

if not negative:
    r = matrix[1][1][n%2]
    for i in xrange(1,n+1):
        for j in xrange(1,n+1):
            r = min(r, matrix[i][j][n%2])

print r if not negative else 'NEGATIVE'
