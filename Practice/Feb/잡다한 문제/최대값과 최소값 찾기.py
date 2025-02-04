# 리스트 numbers에서 최댓값과 최솟값을 반환하는 함수를 작성하세요.

def find_max_min(numbers):
    min_result = min(numbers)
    max_result = max(numbers)
    return (max_result, min_result)

# 테스트 코드
print(find_max_min([3, 1, 7, 9, 2]))  # (9, 1)
print(find_max_min([-5, -1, -9, -3]))  # (-1, -9)
