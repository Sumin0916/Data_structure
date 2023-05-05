from quickSort import *
from mergeSort import *

def do_sort(input_file):
    data_file = open(input_file)
    A = []
    iscache = dict()

    for line in data_file.readlines():
        lpn = line.split()[0]
        inlpn = int(lpn)
        if inlpn not in iscache:
            iscache[inlpn] = 0
            A.append(inlpn)
        iscache[inlpn] += 1

    for i in range(10):
        print(A[i], end=' ')
    print()

    B = quickSort(A, iscache)

    for i in range(10):
        print(f"({B[i]}, {iscache[B[i]]})", end=' ')
    print()

    C = mergeSort(A, iscache)

    for i in range(10):
        print(f"({C[i]}, {iscache[C[i]]})", end=' ')
    print()



if __name__ == "__main__":
    do_sort("C:\\Users\\gsmin2020\\Desktop\\SoongSilUniv\\2-1\\Data_structure\\practice\\linkbench_short.trc")