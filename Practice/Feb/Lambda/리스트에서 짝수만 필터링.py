# 주어진 리스트에서 짝수만 남긴 새로운 리스트를 반환하는 함수를 작성하세요.

def filter_even(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

# 테스트
print(filter_even([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
print(filter_even([10, 15, 20, 25]))  # [10, 20]
