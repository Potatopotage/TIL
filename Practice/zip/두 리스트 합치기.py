# 두 개의 리스트 list1과 list2가 주어졌을 때, 각 인덱스의 요소를 튜플로 묶은 리스트를 반환하세요.

def pair_elements(list1, list2):
    return list(zip(list1, list2))

# 테스트
print(pair_elements([1, 2, 3], ['a', 'b', 'c']))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print(pair_elements([10, 20], [100, 200, 300]))  # [(10, 100), (20, 200)]
