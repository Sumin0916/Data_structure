import math

def insertionSort(A):
    for i in range(1, len(A)):
        loc = i - 1
        newItem = A[i]
        while 0 <= loc and newItem < A[loc]:
            A[loc+1] = A[loc]
            loc -= 1
        A[loc+1] = newItem

def bucketSort(A):
    n = len(A)
    B = [[] for _ in range(n)]
    for i in range(n):
        B[math.floor(A[i]*n)].append(A[i])
    A.clear()
    for i in range(n):
        insertionSort(B[i])
        A.extend(B[i])

if __name__ == "__main__":
    A = [0.98, 0.1, 0.543, 0.713, 0.3333, 0.4444, 0.1, 0.113]
    bucketSort(A)
    print(A)