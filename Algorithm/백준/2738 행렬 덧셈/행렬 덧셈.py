"""
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

첫째 줄에 행렬의 크기 N 과 M이 주어진다.
둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
"""

A, B = map(int, input().split())

arr_A = [list(map(int, input().split()))for _ in range(A)]
arr_B = [list(map(int, input().split()))for _ in range(B)]

result = [[0] * A for _ in range(A)]

for r in range(A):
    for c in range(A):
        result[r][c] = arr_A[r][c] + arr_B[r][c]

for lst in result:
    print(*lst)