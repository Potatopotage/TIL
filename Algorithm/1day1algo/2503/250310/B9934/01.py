"""
이 도시의 도로는 깊이가 K인 완전 이진 트리를 이루고 있다
깊이가 K인 완전 이진 트리는 총 2 ** K - 1개의 노드로 이루어져있다
각 노드에는 그곳에 위치한 빌딩의 번호가 붙여져 있다

도시 방문 순서
1. 트리의 루트
2. 현재 빌딩의 왼쪽 자식에 있는 빌딩에 들어가지 않았다면, 왼쪽 자식으로 이동
3. 현재 있는 노드가 왼쪽 자식을 가지고 있지 않거나, 왼쪽 자식에 있는 빌딩을 이미 들어갔다면
   현재 노드에 있는 빌딩을 들어가고 종이에 번호를 적는다
4. 현재 빌딩을 이미 들어갔다 온 상태이고, 오른쪽 자식을 가지고 있는 경우에는 오른쪽 자식으로 이동한다
5. 현재 빌딩과 왼쪽, 오른쪽 자식에 있는 빌딩을 모두 방문했다면, 부모 노드로 이동한다

방문한 도시의 순서가 주어졌을 때, 각 레벨에 있는 빌딩의 번호를 구하는 프로그램을 작성하시오

입력
K
방문한 빌딩의 번호가 순서대로
"""
from collections import deque
import sys
input = sys.stdin.readline

def build_tree(visited):
    if not visited:
        return None

    mid = len(visited) // 2
    current_root = visited[mid]

    left_tree = build_tree(visited[:mid])
    right_tree = build_tree(visited[mid + 1:])

    return {'val': current_root, 'left': left_tree, 'right': right_tree}

def print_tree_by_level(tree, k):
    if not tree:
        return

    queue = deque([(tree, 0)])
    levels = [[] for _ in range(K)]

    while queue:
        node, level = queue.popleft()

        if level < K:
            levels[level].append(str(node['val']))

            if node['left']:
                queue.append((node['left'], level + 1))
            if node['right']:
                queue.append((node['right'], level + 1))

    for line in levels:
        print(' '.join(line))



K = int(input())
visited = list(map(int, input().split()))
tree = build_tree(visited)

# 레벨별 출력
print_tree_by_level(tree, K)

"""
1
2 3
"""