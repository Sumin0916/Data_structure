def insertionSort(A):
    for i in range(1, len(A)):
        loc = i-1
        newItem = A[i]
        while loc >= 0 and newItem < A[loc]:
            A[loc+1] = A[loc]
            loc -= 1
        A[loc+1] = newItem

if __name__ == "__main__":
    A = [1,5,2,7,1,0,1,2,11,-3]
    insertionSort(A)
    print(A)
