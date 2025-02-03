# 주어진 문자열 리스트 words에서 각 단어의 길이를 리스트로 반환하세요.

def word_lengths(words):
    return list(map(len, words))

# 테스트
print(word_lengths(["apple", "banana", "kiwi"]))  # [5, 6, 4]
print(word_lengths(["hello", "world"]))  # [5, 5]