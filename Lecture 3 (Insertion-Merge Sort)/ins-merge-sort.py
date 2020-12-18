def insertion_sort(arr):
    for i in range(1, len(arr)):
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr


ex = [5, 1, 3, 6, 8, 35, 7, 1, 37, 23]


def merge(left, right):
    i, j, res = 0, 0, []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:]) if i < len(left) else res.extend(right[j:]) if j < len(right) else 0
    return res


def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    left, right = merge_sort(arr[:n // 2]), merge_sort(arr[n // 2:])
    return merge(left, right)


print(merge_sort(ex))
