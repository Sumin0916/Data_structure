def quickSort(p:int, r:int):
    if p < r:
        q = partition(p, r)
        quickSort(p, q)
        quickSort(q+1, r)

def partition():
    
if __name__ == "__main__":
    A = [1,5,2,7,1,0,1,2,11,-3]
    quickSort(A, 0, len(A)-1)
    print(A)
