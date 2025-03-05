"""
이진 트리를 입력받아
전위 순회(preorder traversal): 부모노드>좌>우
중위 순회(inorder traversal): 왼>부>오
후위 순회(postorder traversal): 좌>우>부
한 결과를 출력하는 프로그램을 작성하시오.
"""
import sys
input = sys.stdin.readline

# 전위순회
def preorder(node):
    # 노드가 '0'이라면 자식이 없으므로 그대로 return
    if node == '.':
        return
    # 부모노드(현재노드)를 전위순회 리스트에 추가
    preorder_lst.append(node)
    # 왼쪽 자식 탐색
    preorder(tree[node][0])
    # 오른쪽 자식 탐색
    preorder(tree[node][1])

# 중위순회
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    inorder_lst.append(node)
    inorder(tree[node][1])

# 후위순회
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    postorder_lst.append(node)

N = int(input())
arr = [list(input().split()) for _ in range(N)]


tree = {}

# 노드 정보를 딕셔너리에 저장
# 딕셔너리의 키: 부모노드
# 딕셔너리의 값: 자식노드
for lst in arr:
    parent, left, right = lst
    tree[parent] = (left, right)


# 각 노드를 탐색할 때마다 담아줄 리스트
preorder_lst = []
inorder_lst = []
postorder_lst = []

node = 'A'

# 함수 실행
preorder(node)
inorder(node)
postorder(node)

# 양식에 맞게 출력
print(''.join(preorder_lst))
print(''.join(inorder_lst))
print(''.join(postorder_lst))



"""
ABDCEFG
DBAECFG
DBEGFCA
"""