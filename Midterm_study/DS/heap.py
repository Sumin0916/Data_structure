class Heap:
    def __init__(self, *arg):
        self.__A = []
        if len(arg) != 0:
            self.__A = arg[0]
        self.__numItems = 0

    def insert(self, x):
        self.__A.append(x)
        self.__numItems += 1
        self.__percolateUp(self.__numItems-1)

    def __percolateUp(self, ind:int):
        parent = (ind-1)//2
        if (-1 < ind < self.__numItems) and (self.__A[parent] < self.__A[ind]):
            self.__A[parent], self.__A[ind] = self.__A[ind], self.__A[parent]
            self.__percolateUp(parent)
    
    def __percolateDown(self, ind:int):
        child = 2*ind + 1
        rchild = 2*ind + 2
        if child < self.__numItems:
            if (rchild < self.__numItems) and (self.__A[child] < self.__A[rchild]):
                child = rchild
            if self.__A[child] > self.__A[ind]:
                self.__A[child], self.__A[ind] = self.__A[ind], self.__A[child]
                self.__percolateDown(child)

    def deleteMax(self):
        if not self.isEmpty():
            rm = self.__A[0]
            self.__A[0] = self.__A.pop()
            self.__numItems -= 1
            self.__percolateDown(0)
            return rm
        else:
            print("There is no elements")

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




