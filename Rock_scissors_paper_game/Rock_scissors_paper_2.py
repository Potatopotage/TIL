import random

def random_string_picker(strings):
    return random.choice(strings)

predefined_strings = ["가위", "바위", "보"]
result = random_string_picker(predefined_strings)
# print(result)

def user_choice():
    print('메뉴를 선택해주세요')
    print('1. 게임 실행')
    print('2. 프로그램 종료')
    user_input_choice = input('>')
    if user_input_choice == '1':
        result_rsp(user_input_choice)
    elif user_input_choice == "2":
        print('프로그램이 종료됩니다')
    else:
        print('알맞은 숫자를 입력해주세요')
        user_choice()




def result_rsp(user_input):

    print('가위바위보!')

    user_input = input('>')

    if user_input == '가위':
        if result == '가위':
            print('비겼습니다')
        elif result == '바위':
            print('이겼습니다')
        elif result == '보':
            print('졌습니다')
    elif user_input == '바위':
        if result == '가위':
            print('졌습니다')
        elif result == '바위':
            print('비겼습니다')
        elif result == '보':
            print('이겼습니다')
    elif user_input == '보':
        if result == '보':
            print('비겼습니다')
        elif result == '가위':
            print('이겼습니다')
        elif result == '바위':
            print('졌습니다')
    else:
        print('알맞은 단어를 입력해주세요')
        result_rsp(user_input)


user_choice()