import random

# 입력값 타입 확인 
def type_validate(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False

# 입력 & 오류 처리 
def start_number_input():
    print('시작 숫자를 입력해주세요')
    start_number = input('>')
    if type_validate(start_number):
        return start_number
    else:
        print('숫자만 입력해주십시오')
        return start_number_input()

start_number = int(start_number_input())

def end_number_input():
    print('종료 숫자를 입력해주세요')
    end_number = input('>')
    if type_validate(end_number):
        return end_number
    else:
        print('숫자만 입력해주십시오')
        start_number_input()
        return end_number_input()
    
end_number = int(end_number_input())

def generate_number_input():
    print('생성할 숫자의 개수를 입력해주세요')
    generate_number = input('>')
    if type_validate(generate_number):
        return generate_number
    else:
        print('숫자만 입력해주십시오')
        start_number_input()
        return generate_number_input()

generate_number = int(generate_number_input())

def allow_repetition():
    print('중복 생성을 허용하시겠습니까? y/n')
    y_n_input = input('>')
    if y_n_input == 'y':
        return y_n_input
    elif y_n_input == 'n':
        return y_n_input
    else:
        print('y와 n 중 입력해주십시오')
        return allow_repetition()

y_n_input = allow_repetition()


def random_generator():
    global start_number, end_number, generate_number, y_n_input

    generate_number_list = []

    # 중복 허용 
    if y_n_input == 'y':
        pass
    # 중복 비허용 
    elif y_n_input == 'n':
        pass
    return generate_number_list.sort()

result = random_generator()
print(result)