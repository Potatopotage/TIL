from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
N, K = map(int, input().split())

# 수빈이는 앞, 뒤 혹은 두 배를 갈 수 있고 동생은 그대로 있음
# 그러니까 DFS를 사용하면 될 거 같은디,,,? 아마...? 아닌가...?
# 아아아 BFS를 써서 앞, 뒤, 두 배 자리에 동생이 있는 지 봐, 없으면 1 더하고 또 같은 방법으로 탐색해
# 논리는 알겠는데 이걸 구현을 해야한단 말이야


def bfs(N, K):
    queue = deque([N])
    move = 0

    while queue:
        current_spot = queue.popleft()

        if current_spot == K:
            return move

        if 0 <= current_spot - 1 <= 100000:
            queue.append(current_spot - 1)
            move += 1
        if 0 <= current_spot + 1 <= 100000:
            queue.append(current_spot + 1)
            move += 1
        if 0 <= 2 * current_spot <= 100000:
            queue.append(2 * current_spot)
            move += 1

print(bfs(N, K))






"""
4
"""