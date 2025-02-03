# 문자열로 이루어진 숫자 리스트가 주어졌을 때, 이를 정수 리스트로 변환하는 함수를 작성하세요.
# 숫자가 아닌 문자가 포함되어 있다면 해당 원소는 건너뛰세요.

def convert_to_int_list(my_list):
    # 빈 리스트
    final_list = []
    # int 변환 시도
    for each_value in my_list:
        try:
            int(each_value)
            # 변환 성공시 final_list에 추가 
            final_list.append(int(each_value))
        except ValueError:
            pass
    return final_list

print(convert_to_int_list(["1", "2", "three", "4", "five"])) # [1, 2, 4]
print(convert_to_int_list(["10", "20", "thirty", "40"])) # [10, 20, 40]
print(convert_to_int_list(["a", "b", "c"])) # []
