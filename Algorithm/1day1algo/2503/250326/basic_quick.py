arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quicksort(start, end, arr):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] < arr[pivot]:
            left += 1

        while right > start and arr[right] > arr[pivot]:
            right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]

        else:
            arr[left], arr[right] = arr[right], arr[left]

    quicksort(start, right - 1, arr)
    quicksort(right + 1, end, arr)


quicksort(0, len(arr) - 1, arr)

print(arr)
