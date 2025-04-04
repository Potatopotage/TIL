"""
평면에 네 개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다.
이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고,
겹쳐 있을 수도 있고, 하
나가 다른 하나를 포함할 수도 있으며,
변이나 꼭짓점이 겹칠 수도 있다.

이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.
"""
# import pprint
import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = 100

arr = [[0] * N for _ in range(N)]
squares = [list(map(int, input().split())) for _ in range(4)]

for square in squares:
    c1, r1, c2, r2 = square
    for i in range(r1, r2):
        for j in range(c1, c2):
            arr[i][j] = 1

cnt = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            cnt += 1

print(cnt)





"""
26
"""