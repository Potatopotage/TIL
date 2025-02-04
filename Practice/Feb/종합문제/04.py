# 딕셔너리 메서드 활용: 두 개의 딕셔너리를 병합하는 함수를 작성하시오.

def merge_dicts(dict1, dict2):
    # 최종 딕셔너리
    final_dict = {}

    # dict1의 key와 value를 먼저 담는다
    for key, value in dict1.items():
        if key not in final_dict:
            final_dict[key] = value
    
    # dict2의 key와 value를 담는다
    for key, value in dict2.items():
        if key not in final_dict:
            final_dict[key] = value

    return final_dict

# 예시 입력: merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
# 예시 출력: {'a': 1, 'b': 3, 'c': 4}

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))