def quickSort(A, p:int, r:int):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

def partition(A, p:int, r:int):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] < x:
            i+=1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

if __name__ == "__main__":
    A = [1,5,2,7,1,0,1,2,11,-3]
    quickSort(A, 0, len(A)-1)
    print(A)
