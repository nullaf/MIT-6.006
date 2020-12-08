def peak1d(arr):
    start, stop = 0, len(arr)
    while True:
        mid = (start + stop) // 2
        if mid > 0 and arr[mid] < arr[mid - 1]:
            stop = mid
        elif mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
            start = mid
        else:
            return mid


def peak2d(arr):
    start, stop = 0, len(arr)
    while True:
        row = (start + stop) // 2
        col = peak1d(arr[row])
        if row > 0 and arr[row][col] < arr[row - 1][col]:
            stop = row
        elif row < len(arr) - 1 and arr[row][col] < arr[row + 1][col]:
            start = row
        else:
            return arr[row][col]
