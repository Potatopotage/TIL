"""
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다.
농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에,
한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다.
이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다.
특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어,
그 배추들 역시 해충으로부터 보호받을 수 있다.
한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다.
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로
서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.
0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.
"""

import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

from collections import deque


def bfs(r, c, N, M):
    global field
    queue = deque([(r, c)])
    field[r][c] = 0

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    while queue:
        current_r, current_c = queue.popleft()

        for i in range(4):
            nr = current_r + dr[i]
            nc = current_c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if field[nr][nc] == 1:
                    field[nr][nc] = 0
                    queue.append((nr, nc))

    return 1


T = int(input())

for test_case in range(1, T + 1):
    # M: 배추밭의 가로 길이
    # N: 배추밭의 세로 길이
    # K: 배추가 심어져 있는 위치의 개수
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        c, r = map(int, input().split())
        field[r][c] = 1

    count_warm = 0
    for r in range(N):
        for c in range(M):
            if field[r][c] == 1:
                bfs(r, c, N, M)
                count_warm += 1

    print(count_warm)












"""
5
1
"""