"""
로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 만드시오
청소기는 바라보는 방향이 있다

청소기의 작동 방식
1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다
2. 현재 칸의 주변 4칸 중 아직 청소되지 않은 칸이 없는 경우,
    1. 바라보는 칸을 기준으로 후진할 수 있다면 후진한 후, 1번으로 돌아간다
    2. 후진할 수 없다면 작동을 멈춘다
3. 현재 칸의 주변 4칸 중 아직 청소되지 않은 칸이 있는 경우,
    1. 반시계 방향으로 90도 회전한다
    2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 경우 한 칸 전진한다
    3. 1번으로 돌아간다

모두 청소됐으면 후진을 하고 청소되지 않은 칸이 있으면 반시계방향(왼쪽)으로 돌면서 전진
"""
import sys
sys.stdin = open('BOJ14503.txt', 'r')

def clean(r, c, d):
    # 청소한 한 횟수
    cnt = 0
    # 일단 돌려
    while True:
        # 현재 방 청소 안 했으면 청소(2) 후 카운트
        if rooms[r][c] == 0:
            rooms[r][c] = 2
            cnt += 1

        # 반 시계 방향으로 돌려가면서 청소 안 되어있고 갈 수 있다면 진행
        for _ in range(4):
            d = (d + 3) % 4
            dr, dc = direction[d]
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M and rooms[nr][nc] == 0:
                r, c = nr, nc
                break

        # 다 청소 되어있으면 후진
        else:
            back_d = (d + 2) % 4
            br, bc = r + direction[back_d][0], c + direction[back_d][1]
            if 0 <= br < N and 0 <= bc < M and rooms[br][bc] != 1:
                r, c = br, bc
            # 뒤로 못 가면 끗
            else:
                break

    return cnt

direction = {
    0: (-1, 0),  # 북
    1: (0, 1),   # 동
    2: (1, 0),   # 남
    3: (0, -1),  # 서
}


# 방의 크기 NxM
# 세로 N 가로 M
N, M = map(int, input().split())

# 로봇청소기가 있는 칸의 좌표와 처음에 로봇청소기가 바라보는 방향 d
# 북쪽 0, 동쪽 1, 남쪽 2, 서쪽 3
start_r, start_c, start_d = map(int, input().split())

# 각 장소의 상태
# 빈칸 0 벽 1
rooms = [list(map(int, input().split())) for _ in range(N)]

ans = clean(start_r, start_c, start_d)

print(ans)

"""
1
"""