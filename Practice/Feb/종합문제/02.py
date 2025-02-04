# 재귀 함수: 피보나치 수열의 n번째 항을 반환하는 함수를 작성하시오.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 예시 입력: fibonacci(6)
# 예시 출력: 8

print(fibonacci(6))