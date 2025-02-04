# 주어진 문자열에서 특정 문자를 모두 제거하는 함수를 작성하세요.

def remove_character(string, char):
    # string을 list로 변환
    string = list(string)

    # list에서 특정 문자열이 list 안에 존재하는 동안 제거
    while char in string:
        string.remove(char)
    
    # 리스트를 str 형태로 변환하여 출력
    return ''.join(string)

print(remove_character("hello world", "o")) # "hell wrld"
print(remove_character("banana", "a")) # "bnn"
print(remove_character("mississippi", "s")) # "miippi"
