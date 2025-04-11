"""
0 길
1 벽
2 출발점
3 도착점

도달 가능 1
도달 불가능 0
"""
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def maze(r, c):
    queue = deque([(r, c)])
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while queue:
        curr_r, curr_c = queue.popleft()

        if arr[curr_r][curr_c] == 3:
            return 1

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if (arr[nr][nc] == 0 or arr[nr][nc] == 3) and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
    return 0




N = 16
T = 10
for _ in range(1, T + 1):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                print(f'#{tc} {maze(r, c)}')
                break
        else:
            continue
        break



"""
#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 1
#9 1
#10 1
"""