"""
이진 검색 트리를 전위  순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오

조건
1. 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다
2. 노드의 오른쪽 서브트리에 있는 모든 키는 노드의 키보다 크다
"""
import sys

def build_tree(preorder_lst):
    if not preorder_lst:
        return []

    root = preorder_lst[0]

    left_tree = []
    right_tree = []
    for node in preorder_lst[1:]:
        if node < root:
            left_tree.append(node)
        elif node > root:
            right_tree.append(node)

    left = build_tree(left_tree)
    right = build_tree(right_tree)

    return [root, left, right]

def postorder(tree):
    if not tree:
        return

    postorder(tree[1])
    postorder(tree[2])

    postorder_lst.append(tree[0])


sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

preorder_lst = []
while True:
    try:
        preorder_lst.append(int(input()))
    except:
        break

tree = build_tree(preorder_lst)
postorder_lst = []
postorder(tree)

for node in postorder_lst:
    print(node)




"""
5
28
24
45
30
60
52
98
50
"""