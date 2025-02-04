# 리스트 메서드 활용: 리스트 내 숫자들을 문자열로 변환한 후, 하나의 문자열로 합쳐 반환하는 함수를 작성하시오.

def concatenate_numbers(lst):
    result = list(map(str, lst))
    return ''.join(result)



# 예시 입력: [1, 2, 3, 4]
# 예시 출력: "1234"

print(concatenate_numbers([1, 2, 3, 4]))