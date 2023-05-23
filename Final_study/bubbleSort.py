def bubbleSort(A):
    for numElements in range(len(A), 0, -1):
        for i in range(numElements-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

if __name__ == "__main__":
    A = [1,5,2,7,1,0,1,2,11,-3]
    bubbleSort(A)
    print(A)
