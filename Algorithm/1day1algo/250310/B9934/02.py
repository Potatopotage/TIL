"""
중위 탐색한 결과로 트리 정보를 저장 후 K만큼 한 줄 씩 출력
"""
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

# 중위 순회한 결과로 원 트리를 출력하는 함수
def build_tree(visited):
    if not visited:
        return None

    mid = len(visited) // 2
    current_node = visited[mid]

    left_tree = build_tree(visited[:mid])
    right_tree = build_tree(visited[mid + 1:])

    return {'value': current_node, 'left': left_tree, 'right': right_tree}

def read_tree(tree, K):
    if not tree:
        return
    result = [[] for _ in range(K)]
    queue = deque([(tree, 0)])

    while queue:
        current_node, level = queue.popleft()

        if level < K:
            result[level].append(str(current_node['value']))

            if current_node['left']:
                queue.append((current_node['left'], level + 1))
            if current_node['right']:
                queue.append((current_node['right'], level + 1))

    for line in result:
        print(' '.join(line))


K = int(input())
visited = list(map(int, input().split()))

tree = build_tree(visited)

read_tree(tree, K)

