def find_parent(parent_list, x):
    # 부모가 자기 자신일 때까지 따라간다
    while parent_list[x] != x:
        x = parent_list[x]
    return x


def union_parent(parent_list, a, b):
    root_a = find_parent(parent_list, a)
    root_b = find_parent(parent_list, b)
    if root_a != root_b:
        # 간단히 a 루트를 b 루트에 연결
        parent_list[root_b] = root_a


# 사용 예시
n = 5
parent = [i for i in range(n + 1)]  # 1~5

print(parent)

union_parent(parent, 1, 2)
union_parent(parent, 2, 3)

print(find_parent(parent, 3))  # 1 (root)
