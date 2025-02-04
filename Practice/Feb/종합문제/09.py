# 튜플 조작: 리스트의 요소를 튜플로 묶어 반환하는 함수를 작성하시오.

def pairwise_tuples(lst):
    str_lst = list(map(str, lst))

    odd_list = []
    even_list = []

    if len(str_lst) % 2 == 0:
        for i in range(len(str_lst)):
            if (i + 1) % 2 == 1:
                odd_list.append(str_lst[i])
            else:
                even_list.append(str_lst[i])
        pair = list(zip(odd_list, even_list))

        result_data = [(int(a), int(b)) for a, b in pair]

        
        return result_data
    
    else:
        for i in range(len(str_lst)):
            if (i + 1) % 2 == 1:
                odd_list.append(str_lst[i])
            else:
                even_list.append(str_lst[i])
            
        even_list.append(None)
        
        pair = list(zip(odd_list, even_list))
        result_data = [(int(a), int(b)) if b is not None else (int(a), None) for a, b in pair]

        return result_data

        


# 예시 입력: [1, 2, 3, 4, 5]
# 예시 출력: [(1, 2), (3, 4), (5, None)]

print(pairwise_tuples([1, 2, 3, 4, 5]))
