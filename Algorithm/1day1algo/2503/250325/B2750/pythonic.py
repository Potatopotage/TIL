import sys
sys.stdin = open('input.txt', 'r')

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)

N = int(input())
array = [int(input()) for _ in range(N)]

print(quicksort(array))
