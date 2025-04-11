"""
G: RC카가 이동 가능한 땅
T: RC카가 이동이 불가능한 나무
X: 현재 RC카의 위치
Y: RC카를 이동시키고자 하는 위치

A: 앞으로 이동
L: 현재 바라보고 있는 방향에서 왼쪽으로 90도 회전
R: 현재 바라보고 있는 방향에서 오른쪽으로 90도 회전

RC카를 조종한 커맨드가 주어졌을 때, 목적지에 도달할 수 있는지 구하라
커맨드가 종료되었을 때, 목적지에 위치해 있어야 한다
"""

import sys
sys.stdin = open('input.txt', 'r')

def drive(C, commends, start_r, start_c):

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    direction = 0

    r, c = start_r, start_c
    for cmd in commends:
        if cmd == 'A':
            nr = r + dr[direction]
            nc = c + dc[direction]

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] in ('G', 'Y'):
                r, c = nr, nc

        elif cmd == 'L':
            direction = (direction + 3) % 4
        elif cmd == 'R':
            direction = (direction + 1) % 4

    return int(arr[r][c] == 'Y')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    Q = int(input())

    result = []
    for _ in range(Q):
        C, commends = input().split()

        for r in range(N):
            for c in range(N):
                if arr[r][c] == 'X':
                    start_r = r
                    start_c = c
                    break
            else:
                continue
            break
        result.append((drive(C, commends, start_r, start_c)))

    print(result)


"""
#1 1 0 1
"""