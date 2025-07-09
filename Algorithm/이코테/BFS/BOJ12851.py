"""
수빈이는 현재 점 N에 있고, 동생은 점 K에 있다
수빈이는 걷거나 순간이동을 할 수 있다
만약 수빈이의 위치가 X일 때 걷는다면 X - 1 또는 X + 1로 이동하게 된다
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후 인지, 가장 빠른 시간으로 찾는 방법이 몇 가지인지 구하는 프로그램을 작성
"""
import sys
sys.stdin = open('BOJ12851.txt', 'r')

from collections import deque

# bfs
# chase_start 수빈이의 출발 지점
# run 동생이 숨어있는 곳
def bfs(chase_start, run):

    # 최대 입력값
    max_position = 100001

    # 이동 횟수를 기록
    visited = [0] * max_position
    # 최소 횟수로 도달한 방법의 수를 기록
    count = [0] * max_position

    # 초기값 지정
    visited[chase_start] = 1
    count[chase_start] = 1
    queue = deque([chase_start])

    while queue:
        curr = queue.popleft()

        # 이동
        for next_pos in [curr - 1, curr + 1, curr * 2]:
            # 범위 안에 있는지 확인
            if 0 <= next_pos < max_position:
                # 처음 도착한 경우
                if visited[next_pos] == 0:
                    # 최소 이동 횟수 기록
                    visited[next_pos] = visited[curr] + 1
                    # 이동한 경우의 수는 같다
                    count[next_pos] = count[curr]
                    # 큐에 넣기
                    queue.append(next_pos)
                # 도착했던 곳인데 최소 이동 횟수인 경우
                elif visited[next_pos] == visited[curr] + 1:
                    # 경우의 수 누적
                    count[next_pos] += count[curr]

    # 동생이 숨어있는 곳의 최소이동횟수와 그 경우의 수 return
    return visited[run] - 1, count[run]

N, K = map(int, input().split())

result_1, result_2 = bfs(N, K)

print(result_1)
print(result_2)


"""
4
2
"""