# 주어진 정수 리스트 numbers의 각 요소를 제곱한 리스트를 반환하는 함수를 작성하세요.

def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))

# 테스트
print(square_numbers([1, 2, 3, 4]))  # [1, 4, 09, 16]
print(square_numbers([-1, -2, 0, 5]))  # [1, 4, 0, 25]