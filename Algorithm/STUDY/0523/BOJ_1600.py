"""
말은 격자판에서 체스의 나이트와 같은 이동방식을 가진다.
다음 그림에 말의 이동방법이 나타나있다.
X표시한 곳으로 말이 갈 수 있다는 뜻이다.
참고로 말은 장애물을 뛰어넘을 수 있다

그러나 말은 저렇게 움직일 수 있지만 원숭이는 능력이 부족해서 총 K번만 위와 같이 움직일 수 있고,
그 외에는 그장 인접한 칸으로만 움직일 수 있다(대각선x)

원숭이는 격자판 맨 왼쪽 위에서 시작해서 맨 오른쪽 아래까지 가야한다
인접한 네 방향으로 한 번 움직이는 것, 말의 움직임으로 한 번 움직이는 것, 모두 한 번의 동작으로 친다
격자판이 주어졌을 때, 원숭이가 최소한의 동작으로 시작지넘에서 도착지점까지 갈 수 있는 방법을 알아내는 프로그램을 작성하시오
"""
import sys
sys.stdin = open('1600.txt', 'r')

from collections import deque

# BFS 돌려서 최단 횟수 찾기
def bfs():
    # 방문처리
    # 같은 칸이라도 남은 말 이동 횟수가 다르면 다른 경우의 수이기 때문에 말 이동 가능 횟수까지 3차원 배열으로 생성
    visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]
    # 시작점 넣어주기
    queue = deque([(0, 0, K, 0)])
    visited[0][0][K] = True

    # BFS
    while queue:
        # 앞에서 꺼내기
        curr_r, curr_c, curr_k, curr_cnt = queue.popleft()


        # 도착 지점에 도달하면 바로 횟수 return
        if curr_r == H - 1 and curr_c == W - 1:
            return curr_cnt


        # 인접 이동 하기
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < H and 0 <= nc < W and maps[nr][nc] == 0:
                if not visited[nr][nc][curr_k]:
                    visited[nr][nc][curr_k] = True
                    queue.append((nr, nc, curr_k, curr_cnt + 1))

        # 남은 말 이동 횟수가 있다면 말 이동 하기
        if curr_k > 0:
            for dr, dc in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < H and 0 <= nc < W and maps[nr][nc] == 0:
                    if not visited[nr][nc][curr_k - 1]:
                        visited[nr][nc][curr_k - 1] = True
                        queue.append((nr, nc, curr_k - 1, curr_cnt + 1))

    # 도착지점에 도착하지 못했다면 -1 반환
    return -1

K = int(input())
W, H = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(H)]

print(bfs())