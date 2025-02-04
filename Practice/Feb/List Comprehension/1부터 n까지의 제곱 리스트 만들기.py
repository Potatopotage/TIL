# 정수 n이 주어지면, 1부터 n까지의 숫자를 제곱한 리스트를 반환하세요.

def squares(n):
    return [(i + 1) ** 2 for i in range(n)]

# 테스트
print(squares(5))  # [1, 4, 9, 16, 25]
print(squares(3))  # [1, 4, 9]