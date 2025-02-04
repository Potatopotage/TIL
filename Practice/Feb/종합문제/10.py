# 람다 함수 활용: 리스트 내 각 숫자를 세제곱한 리스트를 반환하는 함수를 작성하시오.

def cube_numbers(lst):
    return list(map(lambda x: x ** 3, lst))

# 예시 입력: [1, 2, 3, 4]
# 예시 출력: [1, 8, 27, 64]

print(cube_numbers([1, 2, 3, 4]))