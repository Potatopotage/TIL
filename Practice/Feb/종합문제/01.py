# 함수: 리스트 내 각 숫자를 제곱한 새로운 리스트를 반환하는 함수를 작성하시오.

def square_numbers(lst):
    # 제곱한 숫자를 담을 리스트
    result_list = []
    # 리스트의 각 요소 순회
    for number in lst:
        # 제곱한 결과 리스트에 추가
        result_list.append(number ** 2)
    return result_list

# 예시 입력: [1, 2, 3, 4]
# 예시 출력: [1, 4, 09, 16]

result = square_numbers([1, 2, 3, 4])
print(result)