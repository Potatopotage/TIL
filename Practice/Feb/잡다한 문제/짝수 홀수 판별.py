# 정수 n이 주어지면, 짝수면 "Even", 홀수면 "Odd"를 반환하는 함수를 작성하세요.

def even_or_odd(n):
    if n % 2 == 0:
        return 'Even'
    elif n %2 == 1:
        return 'Odd'

# 테스트 코드
print(even_or_odd(10))  # Even
print(even_or_odd(7))   # Odd
