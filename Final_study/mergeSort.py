def mergeSort(A, p:int, r:int):
    if p < r:
        q = (p+r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p:int, q:int, r:int):
    i = p; j = q+1
    lst = []
    while (i <= q) and (j <= r):
        if A[i] > A[j]:
            lst.append(A[j])
            j+=1
        else:
            lst.append(A[i])
            i+=1

    while i <= q:
        lst.append(A[i])
        i+=1

    while j <= r:
        lst.append(A[j])
        j+=1

    A[p:r+1] = lst

if __name__ == "__main__":
    A = [1,5,2,7,1,0,1,2,11,-3]
    mergeSort(A, 0, len(A)-1)
    print(A)
