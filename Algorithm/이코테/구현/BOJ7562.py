"""
나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
"""
import sys
sys.stdin = open('BOJ7562.txt', 'r')

from collections import deque

def bfs():
    visited = [[0] * I for _ in range(I)]
    visited[start_r][start_c] = 1

    queue = deque([(start_r, start_c, 0)])

    while queue:
        curr_r, curr_c, cnt = queue.popleft()

        if curr_r == target_r and curr_c == target_c:
            return cnt

        for dr, dc in [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, -1), (2, 1), (-2, -1), (-2, 1)]:
            new_r, new_c = curr_r + dr, curr_c + dc
            if 0 <= new_r < I and 0 <= new_c < I:
                if visited[new_r][new_c] == 0:
                    visited[new_r][new_c] = 1
                    queue.append((new_r, new_c, cnt + 1))

    return -1

T = int(input())
for _ in range(T):
    # 체스판 한 변의 길이
    I = int(input())
    # 현재 나이트 위치
    start_r, start_c = map(int, input().split())
    # 목표 위치
    target_r, target_c = map(int, input().split())

    print(bfs())

    """
    나이트의 이동 가능 경로
    (1, 2)
    (-1, 2)
    (1, -2)
    (-1, -2)
    (2, -1)
    (2, 1)
    (-2, -1)
    (-2, 1)
    """


"""
5
28
0
"""