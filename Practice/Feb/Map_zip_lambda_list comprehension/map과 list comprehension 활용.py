# 주어진 리스트에서 각 문자열의 길이를 구하고, 그 길이가 5 이상인 단어의 길이만 리스트로 반환하는 코드를 작성하시오.

words = ["apple", "banana", "cat", "dog", "elephant"]

# 출력 예시
# [5, 6, 8]

print(list(map(len,[x for x in words if len(x) >= 5])))