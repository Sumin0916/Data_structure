def selections(lst, n):
    if n == 1:
        return [lst[0]]
    m = 0
    for i in range(n):
        if lst[m] > lst[i]:
            m = i 
    mv = lst[m]
    lst[m], lst[n-1] = lst[n-1] , lst[m]
    return selections(lst, n-1) + [mv]

def m():
max()    

print(selections([1, 3, 0, 3, 5, 6, 5], 7))