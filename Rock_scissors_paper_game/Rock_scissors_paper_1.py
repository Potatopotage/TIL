import random

def random_string_picker(strings):
    return random.choice(strings)

predefined_strings = ["가위", "바위", "보"]
result = random_string_picker(predefined_strings)
# print(result)

user_input = input()

def result_rsp(user_input):

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