# 리스트와 특정 값이 주어질 때, 그 값이 리스트에서 몇 번째로 작은 값인지를 반환하는 함수를 작성하세요.

def find_rank(my_list, value):
    # 몇 번째로 작은 수인지 count할 변수
    count_rank = 1
    # value가 my_list에 있는지 확인
    for each_number in my_list:
        if value in my_list:
            # value와 각 요소 비교하여 vale가 해당 요소보다 클 경우 count 증가
            if each_number < value:
                count_rank += 1
        # value가 my_list에 없다면 -1 반환환
        else:
            return -1

        
    return count_rank

print(find_rank([5, 3, 8, 2, 4], 4)) # 3
print(find_rank([10, 20, 30, 40, 50], 50)) # 5
print(find_rank([1, 1, 2, 2, 3], 2)) # 3
print(find_rank([7, 5, 3, 1], 8)) # -1
