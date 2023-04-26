class Heap:
    def __init__(self, *arg):
        self.__A = []
        if len(arg) != 0:
            self.__A = arg[0]
        self.__numItems = 0
        self.__dictItems = dict()

    def cacheInsert(self, x, cache_size) -> bool:
        if (self.__numItems >= cache_size):
            return False
        self.__dictItems[x] = 1
        self.__A.append(x)
        self.__numItems += 1
        self.__percolateUp(self.__numItems-1)
        return True

    def cacheHit(self, x):
        self.__dictItems[x] += 1

    def isCached(self, x):
        if self.__dictItems.get(x) != None:
            return True
        return False

    def __percolateUp(self, ind:int):
        parent = (ind-1)//2
        if (-1 < ind < self.__numItems) and (self.__dictItems[self.__A[parent]] < self.__dictItems[self.__A[ind]]):
            self.__A[parent], self.__A[ind] = self.__A[ind], self.__A[parent]
            self.__percolateUp(parent)
    
    def __percolateDown(self, ind:int):
        child = 2*ind + 1
        rchild = 2*ind + 2
        if child < self.__numItems:
            if (rchild < self.__numItems) and (self.__dictItems[self.__A[child]] < self.__dictItems[self.__A[rchild]]):
                child = rchild
            if self.__A[child] > self.__A[ind]:
                self.__A[child], self.__A[ind] = self.__A[ind], self.__A[child]
                self.__percolateDown(child)

    def deleteMax(self):
        if not self.isEmpty():
            rm = self.__A[0]
            self.__dictItems.pop(rm)
            self.__A[0] = self.__A.pop()
            self.__numItems -= 1
            self.__percolateDown(0)
            return rm
        else:
            print("There is no elements")

    def deleteMin(self):
        if self.__numItems > 1:
            self.__numItems -= 1
            return self.__dictItems.pop(self.__A.pop())
        else:
            print("There is no elements")
        return None

    def findInd(self, x):
        

    def max(self):
        return self.__A[0]

    def buildHeap(self):
        self.__numItems = len(self.__A)
        for i in range((self.__numItems-2)//2, -1, -1):
            self.__percolateDown(i)

    def isEmpty(self):
        return self.__numItems == 0

    def clear(self):
        self.__A = []
        self.__numItems = 0
        self.__dictItems = dict()
    
    def size(self):
        return self.__numItems

    def printList(self):
        print(self.__A)

    def level(self):
        res = 0
        while (self.__numItems>>res) != 0:
            res += 1
        return res

    def heapPrint(self):
        level = self.level()
        len_lst = 2**level
        for lev in range(level):
            print_lst = [' '] * len_lst
            step = len_lst // ((1<<lev+1) - (1<<lev)) // 2
            for ind in range((1<<lev)-1, (1<<lev+1)-1):
                if ind < self.__numItems:
                    print_lst[step + (step*(ind))] = str(self.__A[ind])
            print(' '.join(print_lst))
        print("=================================================")