import sys
from collections import deque
input = sys.stdin.readline

# 중위 순회한 결과를 바탕으로 트리의 정보를 저장하는 함수
def build_tree(visited):
    # 노드가 존재하지 않는다면 value는 None
    if not visited:
        return None

    # 중위순회는 가장 가운데 값이 루트가 된다
    mid = len(visited) // 2
    current_node = visited[mid]

    # 루트를 기준으로 왼쪽, 오른쪽 서브트리 저장
    left_tree = build_tree(visited[:mid])
    right_tree = build_tree(visited[mid + 1:])

    # value에 현재 루트를, left, right에 자식 서브트리를 각각 저장
    return {'value': current_node, 'left': left_tree, 'right': right_tree}

# 딕셔너리로 저장된 트리의 정보를 읽어 K 만큼 줄별로 출력하는 함수
def read_tree(tree, K):
    # K줄만큼 트리의 노드 정보를 저장할 리스트
    result = [[] for _ in range(K)]
    # 전체 트리(시작점)와 노드 level que에 추가
    queue = deque([(tree, 0)])

    # que가 존재한다면
    while queue:
        # 현재 트리와 level을 que에서 꺼낸다
        node, level = queue.popleft()

        # level이 K보다 작을 때에만 수행(level은 0부터 시작)
        if level < K:
            # 현재 노드를 level에 맞추어 result에 추가
            # 후에 join을 사용하기 때문에 string type으로 추가해준다
            result[level].append(str(node['value']))

            # 왼쪽 노드가 존재한다면, 왼쪽서브트리를 현재트리로 que에 추가
            if node['left']:
                queue.append((node['left'], level + 1))

            # 오른쪽도 마찬가지로 수행
            if node['right']:
                queue.append((node['right'], level + 1))

    # result를 한 줄씩 출력
    for line in result:
        print(' '.join(line))



K = int(input())
visited = list(map(int, input().split()))

tree = build_tree(visited)

read_tree(tree, K)