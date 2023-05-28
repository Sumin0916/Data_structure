class Heap:
    def __init__(self, *args):
        if len(args) != 0:
            self.__A = args[0]
        else :
            self.__A = []
    
    def insert(self, x):
        self.__A.append(x)
        self.__percolateUp(len(self.__A)-1)

    def __percolateUp(self, i:int):
        parent = (i - 1)//2
        if i > 0 and self.__A[i] > self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.__percolateUp(parent)

    def deleteMax(self):
        if (not self.isEmpty()):
            max = self.__A[0]
            self.__A[0] = self.__A.pop()
            self.__percolateDown(0)
            return max
        else :
            return None
        
    def __percolateDown(self, i:int):
        child = 2 * i + 1
        right = 2 * i + 2
        if (child <= len(self.__A)-1):
            if (right <= len(self.__A)-1) and (self.__A[child] < self.__A[right]):
                child = right
            if self.__A[i] < self.__A[child]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.__percolateDown(child)

    def max(self):
        return self.__A[0]

    def buildHeap(self):
        for i in range((len(self.__A) - 2)//2, -1, -1):
            self.__percolateDown(i)

    def isEmpty(self) :
        return len(self.__A) == 0
    
    def clear(self) :
        self.__A = []

    def size(self) :
        return len(self.__A)

    def printList(self) :
      for element in self.__A:
        print(element, end = ' ')
      print()

    def heapPrint(self):
        len_a = len(self.__A)
        max_log = 0
        while (len_a>>max_log) != 0:
            max_log += 1

        for i in range(max_log):
            for j in range((1<<i)-1, (1<<(i+1))-1):
                if j < len_a:
                    print(self.__A[j], end=' ')
            print()
        print("============================================")
