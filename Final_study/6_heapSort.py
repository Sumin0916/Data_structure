def buildHeap(A):
    for i in range((len(A)-2)//2, -1, -1):
        percolateDown(A, i, len(A)-1)

def percolateDown(A, k:int, end:int):
    child = 2*k+1
    right = 2*k+2
    if child <= end:
        if right <= end and A[child] < A[right]:
            child = right
        if A[k] < A[child]:
            A[k], A[child] = A[child], A[k]
            percolateDown(A, child, end)

def heapSort(A):
    buildHeap(A)
    for last in range(len(A)-1, -1, -1):
        A[0], A[last] = A[last], A[0]
        percolateDown(A, 0, last-1)

if __name__ == "__main__":
    A = [1,5,2,7,1,0,1,2,11,-3]
    heapSort(A)
    print(A)