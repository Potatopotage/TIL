"""
연속으로 반복되는 문자를 개수와 함께 압축하여 출력하는 프로그램을 작성하세요.

입력 예시:
aabbbccccd

출력 예시:
a2b3c4d1

"""

arr = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd']

# 키와 개수를 입력하는 딕셔너리를 생성하자

count_dict = {}

for char in arr:
    count_dict[char] = count_dict.get(char, 0) + 1

result = ''.join(f'{key}{value}' for key, value in count_dict.items())

print(result)