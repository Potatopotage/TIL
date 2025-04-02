"""
표의 각 칸에는 지뢰가 있을 수도, 없을 수도 있다
특정 칸을 클릭했을 대, 지뢰가 있는 칸이라면 '파핑 파핑!' 이라는 소리와 함께 게임은 끝난다
지뢰가 없는 칸이라면 변이 맞닿아 있거나 꼭지점이 맞닿아 있는 최대 8칸에 대해 몇 개의 지뢰가 있는지가 0에서 8사이의 숫자로 클릭한 칸에 표시된다
지뢰를 '*'로 지뢰가 없는 칸을 '.'로, 클릭한 지뢰가 없는 칸을 'c'로 나타낸다

지뢰가 있는 칸을 제외한 다른 모든 칸의 숫자들이 표시되려면 최소 몇 번의 클릭을 해야 하느지 구하는 프로그램을 작성하라
"""
import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

# 좌우대각선을 탐색하여 지뢰 개수만큼 표시
def find_bomb(r, c):
    # 지뢰 개수 카운트
    cnt = 0
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위 안에 존재하고 지뢰라면 카운트
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '*':
            cnt += 1

    return cnt

# '0'인 칸을 클릭했을 때 나타나는 숫자에 대한 처리
def find_zero(r, c):
    # cnt 불러오기
    global cnt

    # 덱 초기값 설정
    queue = deque([(r, c)])
    visited[r][c] = 1
    # 클릭 횟수 카운트
    cnt += 1

    while queue:
        curr_r, curr_c = queue.popleft()

        for i in range(8):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            # 범위 내에 있고 방문한 적이 없다면 방문 처리
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    # 값이 0이라면 덱에 추가
                    if arr[nr][nc] == 0:
                        queue.append((nr, nc))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 이동 방향
    dr = [1, -1, 1, 1, -1, -1, 0, 0]
    dc = [-1, 1, 1, 0, -1, 0, 1, -1]

    cnt = 0

    # 각 칸의 숫자 표시
    for r in range(N):
        for c in range(N):
            if arr[r][c] == ".":
                arr[r][c] = find_bomb(r, c)

    visited = [[0] * N for _ in range(N)]

    # 숫자가 표시된 arr에 대해 0이고 방문한 적 없다면 find_zero() 실행
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0 and visited[r][c] == 0:
                find_zero(r, c)


    # 방문한 적 없고, 지뢰가 아니라면 클릭하지 않은 숫자이므로 카운트
    for r in range(N):
        for c in range(N):
            if arr[r][c] != '*' and visited[r][c] == 0:
                cnt += 1



    print(f'#{tc} {cnt}')





"""
#1 2
#2 8
"""