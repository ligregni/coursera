# Library of functions.
# module library

def PARENT(x):
    return (x+1)/2-1

def LEFT(x):
    return (x+1)*2-1

def RIGHT(x):
    return (x+1)*2

class MinHeap:
    def __init__(self):
        self.mapa = dict()
        self.heap = list()
        self.size = 0

    def insert(self, key, item):
        if self.size >= len(self.heap):
            self.heap.append((key, item))
        else:
            self.heap[self.size] = (key, item)
        self.mapa[item] = self.size
        self.size += 1
        self.__raiseitem__(self.size-1)

    def delete(self, item):
        index = self.mapa[item]
        self.__swap__(self.size-1, index)
        self.size -= 1
        self.__sink__(index)
        del self.mapa[item]

    def increase(self, item, key):
        if self.heap[self.mapa[item]][0] > key:
            self.heap[self.mapa[item]] = (key, self.heap[self.mapa[item]][1])
            self.__raiseitem__(self.mapa[item])

    def size(self):
        return self.size

    def empty(self):
        return self.size == 0

    def top(self):
        return self.heap[0]

    def __swap__(self, origin, dest):
        tmp = self.heap[origin]
        self.heap[origin] = self.heap[dest]
        self.heap[dest] = tmp
        self.mapa[self.heap[origin][1]] = origin
        self.mapa[self.heap[dest][1]] = dest

    def __raiseitem__(self, index):
        while index != 0:
            if self.heap[PARENT(index)][0] > self.heap[index][0]:
                self.__swap__(PARENT(index), index)
            index = PARENT(index)

    def __sink__(self, index):
        sunk = True
        while sunk:
            sunk = False
            tmp = index
            if LEFT(index) < self.size and self.heap[LEFT(index)][0] < self.heap[tmp][0]:
                tmp = LEFT(index)
            if RIGHT(index) < self.size and self.heap[RIGHT(index)][0] < self.heap[tmp][0]:
                tmp = RIGHT(index)
            if tmp != index:
                self.__swap__(tmp, index)
                index = tmp
                sunk = True

class Set:
    def __init__(self, n):
        self.array = map(lambda x: [x, 0, 1], range(n))
        self.sets = dict(map(lambda x: [x, 1], range(n)))
        self.count = n

    def union(self, a, b):
        aa = self.find(a)
        bb = self.find(b)
        if aa != bb:
            if self.array[aa][1] <= self.array[bb][1]:
                self.array[bb][1] += 1 if self.array[aa][1] == self.array[bb][1] else 0
                self.array[bb][2] += self.array[aa][2]
                self.array[aa][0] = bb
                self.sets[bb] = self.array[bb][2]
                del self.sets[aa]
            else:
                self.array[bb][0] = aa
                self.array[aa][2] += self.array[bb][2]
                self.sets[aa] = self.array[aa][2]
                del self.sets[bb]
            self.count -= 1

    def find(self, x):
        if self.array[x][0] != x:
            self.array[x][0] = self.find(self.array[x][0])
        return self.array[x][0]

    def getSets(self):
        return self.sets.values()

    def getSetCount(self):
        return len(self.sets)

    def sameSet(self, a, b):
        return self.find(a) == self.find(b)
