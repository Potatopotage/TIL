"""

"""
import pprint
import sys
sys.stdin = open('input.txt', 'r')

# N = 가로, M = 세로
N, M = map(int, input().split())
num = int(input())

arr = [[0] * (2 * N - 1) for _ in range(2 * M - 1)]
for _ in range(num):
    order = list(map(int, input().split()))

    if order[0] == 0:
        cut_idx = order[1] * 2 - 1
        for c in range(2 * N - 1):
            arr[cut_idx][c] = 1
    else:
        cut_idx = order[1] * 2 - 1
        for r in range(2 * M - 1):
            arr[r][cut_idx] = 1

    for r in range(1, 2 * M - 1, 2):
        for c in range(2 * N - 1):
            if arr[r][c] != 1:
                arr[r][c] = 2

    for c in range(1, 2 * N - 1, 2):
        for r in range(2 * M - 1):
            if arr[r][c] != 1:
                arr[r][c] = 2


pprint.pprint(arr)


# def width(N, M, r, c):
#     global arr
#
#     cnt_y = 0
#     for i in range(2 * M - 1):
#
#
# for r in range(2 * M - 1):
#     for c in range(2 * N - 1):
#         if arr[r][c] == 0:




"""
30
"""