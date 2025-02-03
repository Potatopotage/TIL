# 리스트 numbers의 모든 원소를 곱한 결과를 반환하세요.

def multiply_list(numbers):
    
    # 초기값 1 설정
    result = 1
    
    # 각 요소를 순회하며 곱하기
    for num in numbers:
        result *= num
    return result


# 테스트 코드
print(multiply_list([1, 2, 3, 4]))  # 24
print(multiply_list([5, 10, 2]))  # 100
