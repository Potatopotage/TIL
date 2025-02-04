# 리스트 조작: 리스트에서 가장 많이 등장한 요소를 반환하는 함수를 작성하시오.

def most_frequent_element(lst):
    str_list = list(map(str,lst))

    max_count = 0
    for number in str_list:
        each_count = str_list.count(number)
        if each_count > max_count:
            max_count = each_count
            max_number = number
    
    return max_number


# 예시 입력: [1, 3, 3, 3, 2, 2, 1]
# 예시 출력: 3

print(most_frequent_element([1, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1]))