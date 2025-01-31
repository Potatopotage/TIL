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
    start_number = input('>')
    if type_validate(start_number):
        pass
    else:
        print('숫자만 입력해주십시오')
        start_number_input()
    return start_number

start_number = int(start_number_input())

def end_number_input():
    end_number = input('>')
    if type_validate(end_number):
        pass
    else:
        print('숫자만 입력해주십시오')
        start_number_input()
    return end_number
end_number = int(end_number_input())

def generate_number_input():
    generate_number = input('>')
    if type_validate(generate_number):
        pass
    else:
        print('숫자만 입력해주십시오')
        start_number_input()
    return generate_number
generate_number = int(generate_number_input())

# 랜덤 숫자 생성 
def random_generator():
    global start_number, end_number, generate_number
    generate_number_list = []

    # 랜덤숫자 생성
    for i in range(generate_number):
        generated_number = random.randint(start_number, end_number)
        generate_number_list.append(generated_number)

    return generate_number_list

generated_number_list = random_generator()
print(generated_number_list)