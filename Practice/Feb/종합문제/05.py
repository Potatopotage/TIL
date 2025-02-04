# 리스트 정렬: 리스트를 정렬하는데, 짝수는 앞에, 홀수는 뒤에 오도록 정렬하는 함수를 작성하시오.

def sort_even_odd(lst):
    # 홀수를 담을 리스트와 짝수를 담을 리스트 준비
    odd_list = []
    even_list = []
    # 리스트의 요소를 하나씩 순회하여 홀/짝 리스트에 담기
    for number in lst:
        if number % 2 == 0:
            even_list.append(number)
        elif number % 2 == 1:
            odd_list.append(number)
    
    # even_list에 odd_list 추가
    even_list.extend(odd_list)

    return even_list

# 예시 입력: [3, 1, 2, 4, 7, 6]
# 예시 출력: [2, 4, 6, 3, 1, 7]

print(sort_even_odd([3, 1, 2, 4, 7, 6]))