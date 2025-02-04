# 리스트 numbers에서 중복된 요소를 제거하고 정렬된 리스트를 반환하세요.

def remove_duplicates(numbers):
    # 빈 리스트 생성
    result = []

    # 각 요소를 순회하며 해당 요소가 result 리스트에 없을 때에만 추가
    for number in numbers:
        if number not in result:
            result.append(number)
    
    # result 졍렬
    result.sort()
    return result

# 테스트 코드
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates([10, 20, 10, 30, 40, 30]))  # [10, 20, 30, 40]
