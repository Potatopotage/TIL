# 어떤 문자열 리스트가 주어질 때, 각 문자열을 대문자로 변환하고, 길이를 튜플 형태로 반환하는 코드를 작성하시오.

words = ["python", "lambda", "map", "zip"]


# 출력 예시
# [('PYTHON', 6), ('LAMBDA', 6), ('MAP', 3), ('ZIP', 3)]

word_list = list(map(lambda x: x.upper(), words))
print(word_list)

print(list(map(lambda x: (x, len(x)), word_list)))