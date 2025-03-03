"""

"""

import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())
pair_num = int(input())


arr = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(pair_num):
    a, b = map(int, input().split())

    arr[a][b] = 1
    arr[b][a] = 1

def bfs(arr, N):
    stack = [1]
    visited = [1]

    while stack:
        current_node = stack.pop()

        for next_node in range(1, N + 1):
            if next_node not in visited and arr[current_node][next_node] == 1:
                visited.append(next_node)
                stack.append(next_node)

    return visited


print(len(bfs(arr, N)) - 1)



"""
4
"""