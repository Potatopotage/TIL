import random

# 입력 된 문자열 중 랜덤으로 하나를 선택하는 함수 
def random_string_picker(strings):
    return random.choice(strings)

predefined_strings = ["가위", "바위", "보"]
result = random_string_picker(predefined_strings)

# 메뉴 실행 
def user_choice():
    print('메뉴를 선택해주세요')
    print('1. 게임 실행')
    print('2. 프로그램 종료')
    user_input_choice = input('>')

    # 게임을 실행할 경우 result_rsp() 
    if user_input_choice == '1':
        result_rsp(user_input_choice)
    # 프로그램 종료 선택 시 score_count()
    elif user_input_choice == "2":
        score_count()
        print('프로그램이 종료됩니다')
    else:
        print('알맞은 숫자를 입력해주세요')
        # 잘못된 문자열 입력력 시 다시 user_choice()
        user_choice()


# 승적을 카운트 할 변수 
win_count = 0
tie_count = 0
lose_count = 0

# input에 따라 각각의 경우 실행 
def result_rsp(user_input):
    
    global win_count, tie_count, lose_count

    print('가위바위보!')

    user_input = input('>')

    # 이긴 경우, 비긴 경우, 진 경우 각각 카운트
    if user_input == '가위':
        if result == '가위':
            print('비겼습니다')
            tie_count += 1
        elif result == '바위':
            print('이겼습니다')
            win_count += 1
        elif result == '보':
            print('졌습니다')
            lose_count += 1
    elif user_input == '바위':
        if result == '가위':
            print('졌습니다')
            lose_count += 1
        elif result == '바위':
            print('비겼습니다')
            tie_count += 1
        elif result == '보':
            print('이겼습니다')
            win_count += 1
    elif user_input == '보':
        if result == '보':
            print('비겼습니다')
            tie_count += 1
        elif result == '가위':
            print('이겼습니다')
        elif result == '바위':
            win_count += 1
            print('졌습니다')
            lose_count += 1
    else:
        print('알맞은 단어를 입력해주세요')
        result_rsp(user_input)

    # 다시 메뉴 실행 
    user_choice()

    return win_count, tie_count, lose_count


# 승적 기록
def score_count():
    global win_count, lose_count, tie_count

    print('')
    print('승적')
    print('-------')
    print(f'이긴 횟수: {win_count}')
    print(f'비긴 횟수: {tie_count}')
    print(f'진 횟수: {lose_count}')
    print('-------')
    print('')


user_choice()