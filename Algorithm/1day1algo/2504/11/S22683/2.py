import sys
sys.stdin = open('input.txt', 'r')


from collections import deque

# 방향: 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(field, N, K, start, target):
    visited = [[[[False] * (K + 1) for _ in range(4)] for _ in range(N)] for _ in range(N)]
    q = deque()

    sr, sc = start
    tr, tc = target

    q.append((sr, sc, 0, 0, 0))  # r, c, 방향, 벤 나무 수, 조작 횟수
    visited[sr][sc][0][0] = True

    while q:
        r, c, d, cut, cnt = q.popleft()

        if (r, c) == (tr, tc):
            return cnt

        # 1. 앞으로 이동 (A)
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            cell = field[nr][nc]
            if cell == 'G' and not visited[nr][nc][d][cut]:
                visited[nr][nc][d][cut] = True
                q.append((nr, nc, d, cut, cnt + 1))
            elif cell == 'T' and cut < K and not visited[nr][nc][d][cut + 1]:
                visited[nr][nc][d][cut + 1] = True
                q.append((nr, nc, d, cut + 1, cnt + 1))

        # 2. 왼쪽 회전 (L)
        nd = (d - 1) % 4
        if not visited[r][c][nd][cut]:
            visited[r][c][nd][cut] = True
            q.append((r, c, nd, cut, cnt + 1))

        # 3. 오른쪽 회전 (R)
        nd = (d + 1) % 4
        if not visited[r][c][nd][cut]:
            visited[r][c][nd][cut] = True
            q.append((r, c, nd, cut, cnt + 1))

    return -1  # 목적지에 도달할 수 없음

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    field = []
    for i in range(N):
        row = list(input().strip())
        for j in range(N):
            if row[j] == 'X':
                start = (i, j)
                row[j] = 'G'
            elif row[j] == 'Y':
                target = (i, j)
                row[j] = 'G'
        field.append(row)

    result = bfs(field, N, K, start, target)
    print(f"#{tc} {result}")
