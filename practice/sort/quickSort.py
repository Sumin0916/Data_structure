def quickSort(arr, count):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    p = count[pivot]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        n= count[num]
        if n > p:
            lesser_arr.append(num)
        elif n < p:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    equal_arr.reverse()
    return quickSort(lesser_arr, count) + equal_arr + quickSort(greater_arr, count)