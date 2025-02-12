"""
주어진 문자열에서 회문(Palindrome)이 되는 모든 부분 문자열의 개수를 구하세요.
(단일 문자도 회문으로 간주)

입력 예시:
abcba
출력 예시:
7
"""

input_str = 'abcba'
N = len(input_str)
# 회문이 되는지 검사하는 함수
def palindrome(my_star):
    return my_star == my_star[::-1]

count_palindrome = 0
for i in range(1, N + 1):
    for j in range(N - i + 1):
        if palindrome(input_str[j: j + i]):
            count_palindrome += 1

print(count_palindrome)