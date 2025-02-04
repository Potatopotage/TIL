# 정수 n이 주어지면, n번째 피보나치 수를 반환하는 함수를 작성하세요.

def fibonacci(number):
    # number가 1 혹은 2일 경우
    if number == 1 or number == 2:
        return 1
    else:
        a = 1
        b = 1
        for _ in range(number - 2):
            a, b = b, a+b
    return b


# 테스트 코드
print(fibonacci(5))  # 5
print(fibonacci(10)) # 55
