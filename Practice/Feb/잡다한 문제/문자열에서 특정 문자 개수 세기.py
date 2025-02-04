#  문자열 s에서 특정 문자 char의 개수를 세는 함수를 작성하세요.

def count_character(word, char):
    # 카운트할 변수 설정
    count_letter = 0
    # 각 문자 순회
    for letter in word:
        # char이 같은 문자열을 찾으면 카운트가 올라가도록 설정
        if char == letter:
            count_letter += 1

    return count_letter


# 테스트 코드
print(count_character("banana", "a"))  # 3
print(count_character("hello world", "l"))  # 3
