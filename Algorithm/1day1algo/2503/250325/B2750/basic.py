import sys
input = sys.stdin.readline

def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        while right > start and arr[right] > arr[pivot]:
            right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]

        else:
            arr[right], arr[left] = arr[left], arr[right]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

N = int(input())
arr = [int(input()) for _ in range(N)]

quick_sort(arr, 0, len(arr) - 1)

for num in arr:
    print(num)