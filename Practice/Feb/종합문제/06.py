# 문자열 조작: 주어진 문자열에서 중복된 문자를 제거하고 사전순으로 정렬된 문자열을 반환하는 함수를 작성하시오.

def unique_sorted_string(s):
    # 문자열 리스트 전환
    s_list = list(s)

    # 중복되지 않은 리스트를 담을 리스트
    final_list = []

    # 리스트의 요소를 순회하며 final_list에 없는 요소만 추가
    for letter in s_list:
        if letter not in final_list:
            final_list.append(letter)

    # 리스트 오름차순 정렬
    final_list.sort()

    # 리스트 문자열 전환
    return ''.join(final_list)


# 예시 입력: "banana"
# 예시 출력: "abn"

print(unique_sorted_string('banana'))