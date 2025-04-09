"""
가장 왼쪽 위 좌표는 (1, 1) 가장 오른쪽 아래 좌표는 (N, N)에 해당한다
여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다

L: 왼쪽
R: 오른쪽
U: 위
D: 아래

정사각형 공간을 벗어나는 움직임은 무시된다
여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오
"""
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
plans = list(input().split())

direction = {
    'R': (0, 1),
    'L': (0, -1),
    'D': (1, 0),
    'U': (-1, 0)
}

r, c = 0, 0
for plan in plans:
    nr = r + direction[plan][0]
    nc = c + direction[plan][1]

    if 0 <= nr < N and 0 <= nc < N:
        r, c = nr, nc
    else:
        continue

print(r + 1, c + 1)
