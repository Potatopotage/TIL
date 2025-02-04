# 주어진 숫자 리스트에서 짝수는 제곱하고, 홀수는 세 배 한 값을 반환하는 lambda 함수를 작성하시오.

numbers = [1, 2, 3, 4, 5, 6]

# 출력 예시
# [3, 4, 9, 16, 15, 36]

print(list(map(lambda x: x ** 2 if x % 2 == 0 else x * 3, numbers)))