# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):

    blood_types_dict = {}

    for each_blood in blood_types:
        if each_blood in blood_types_dict:
            blood_types_dict[each_blood] += 1
        else:
            blood_types_dict[each_blood] = 1

    return blood_types_dict


print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    blood_count = {}

    for blood in blood_types:
        blood_count[blood] = blood_count.get(blood, 0) + 1
    
    return blood_count


print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
