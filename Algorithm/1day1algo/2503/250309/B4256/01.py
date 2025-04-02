"""
BT를 전위 순회, 중위 순회한 결과가 주어진다
BT를 후위 순회했을 때의 결과를 구하는 프로그램을 작성

전위(preorder): 루트>>왼>>오
중위(inorder): 왼>>부모>>오
후위(postorder): 왼>>오>>부모
"""

import sys
sys.stdin = open('input.txt', 'r')


def build_origin_tree(prorder, inorder):
    if not prorder or not inorder:
        return None
    current_root = prorder[0]
    root_index = inorder.index(current_root)

    left_tree = build_origin_tree(prorder[1:root_index + 1], inorder[:root_index])
    right_tree = build_origin_tree(prorder[root_index + 1:], inorder[root_index + 1:])

    return {"val": current_root, 'left': left_tree, 'right': right_tree}

def postorder(tree):
    if tree is None:
        return []

    left_result = postorder(tree['left'])
    right_result = postorder(tree['right'])

    return left_result + right_result + [tree['val']]


T = int(input())
for tc in range(1, T + 1):
    # n: 노드의 개수
    n = int(input())
    # 전위순회
    preorder = list(map(int, input().split()))
    # 중위순회
    inorder = list(map(int, input().split()))

    print(build_origin_tree(preorder, inorder))
    print(*postorder(build_origin_tree(preorder, inorder)))



"""
2 4 1 3
5 8 4 6 2 1 7 3
"""