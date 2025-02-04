# 두 개의 숫자 리스트 list1과 list2가 주어졌을 때, 각 인덱스의 요소를 더한 리스트를 반환하세요.

def sum_lists(list1, list2):
    pair = zip(list1, list2)
    return list(map(sum, pair))

# 테스트
print(sum_lists([1, 2, 3], [4, 5, 6]))  # [5, 7, 9]
print(sum_lists([10, 20, 30], [1, 2, 3]))  # [11, 22, 33]
