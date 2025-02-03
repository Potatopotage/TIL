# 정수 n이 주어지면, n을 뒤집어서 반환하는 함수를 작성하세요.

def reverse_number(n):
    if n >= 0:
        return (str(n))[::-1]
    else:
        no_minus = (str(n))[1:]
        minus_result = '-' + no_minus[::-1]
        minus_result = int(minus_result)
        return minus_result

# 테스트 코드
print(reverse_number(1234))  # 4321
print(reverse_number(-987))  # -789

