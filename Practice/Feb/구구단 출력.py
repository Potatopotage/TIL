# 정수 n이 주어지면, n단의 구구단을 출력하는 함수를 작성하세요.

def multiplication_table(n):
    # 1부터 9까지 순회하며 구구단 출력
    for i in range(9):
        print(f'{n} * {(i+1)} = {n * (i+1)}')

# 테스트 코드
multiplication_table(3)
