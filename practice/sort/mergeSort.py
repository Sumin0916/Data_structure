def mergeSort(arr,count):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = mergeSort(arr[:mid], count)
    high_arr = mergeSort(arr[mid:], count)

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if count[low_arr[l]] > count[high_arr[h]]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr