# Python의 min() 함수를 사용하지 않고 리스트에서 두 번째로 작은 값을 찾는 함수를 작성하세요.

def second_min_value(my_list):
    
    min_number = my_list[0]
    
    # 최솟값 찾기
    for each_number in my_list:
        if each_number < min_number:
            min_number = each_number
    
    # 최소값 제거
    while min_number in my_list:
        my_list.remove(min_number)

    # 두 번째로 작은 값 찾기
    second_min = my_list[0]
    for each_number in my_list:
        if each_number < second_min:
            second_min = each_number
    return second_min



print(second_min_value([10, 20, 30, 40])) # 20
print(second_min_value([5, 1, 4, 2, 1])) # 2
print(second_min_value([100, 99, 98, 97, 96])) # 97