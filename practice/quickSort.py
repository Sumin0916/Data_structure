def quickSort(arr, count):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        val = count[num]
        pn = count[pivot]
        if val > pn:
            lesser_arr.append(num)
        elif val < pn:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quickSort(lesser_arr, count) + equal_arr + quickSort(greater_arr, count)
