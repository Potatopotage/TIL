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


def end_number_input():
    print('종료 숫자를 입력해주세요')
    end_number = input('>')
    if type_validate(end_number):
        return end_number
    else:
        print('숫자만 입력해주십시오')
        end_number_input()
        return end_number_input()
    


def generate_number_input():
    print('생성할 숫자의 개수를 입력해주세요')
    generate_number = input('>')
    if type_validate(generate_number):
        return generate_number
    else:
        print('숫자만 입력해주십시오')
        generate_number_input()
        return generate_number_input()


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


def random_generator():

    start_number = int(start_number_input())
    end_number = int(end_number_input())

    if start_number > end_number:
        print('종료 숫자는 시작 숫자보다 커야 합니다')
        return random_generator()
    
    generate_number = int(generate_number_input())

    if generate_number > end_number - start_number + 1:
        print('숫자의 범위보다 생성할 숫자의 개수가 더 많습니다')
        return random_generator()

    y_n_input = allow_repetition()

    generate_number_list = []

    # 중복 허용 
    if y_n_input == 'y':
        # generate_number만큼 랜덤 숫자 생성
        for _ in range(generate_number):
            random_number = random.randint(start_number, end_number)
            generate_number_list.append(random_number)
        
        generate_number_list.sort()
        return generate_number_list

    # 중복 비허용 
    elif y_n_input == 'n':
        
        result = random.sample(range(start_number, end_number + 1), generate_number)
        result.sort()
        return result
        

result = random_generator()
print(result)