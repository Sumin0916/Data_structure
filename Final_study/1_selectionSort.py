def selectionSort(A):
    for last in range(len(A)-1, 0, -1): #0은 포함되지 않는다.
        max_ind = theLargest(A, last)
        A[max_ind], A[last] = A[last], A[max_ind]

def theLargest(A, last:int) -> int:
    largest = 0 #이러면 음수는 판별 못하긴해
    for i in range(last+1):
        if A[largest] < A[i]: #가장 먼저 있는 큰값을 바꿔주게된다
            largest = i
    return largest

if __name__ == "__main__":
    A = [1,5,2,7,1,0,1,2,11,-3]
    selectionSort(A)
    print(A)
