# 주어진 문자열 리스트에서 길이가 5 이상인 단어만 포함된 리스트를 반환하세요.

def filter_long_words(words):
    return [word for word in words if len(word) >= 5]

# 테스트
print(filter_long_words(["apple", "hi", "banana", "ok", "grape"]))  # ["apple", "banana", "grape"]
print(filter_long_words(["hello", "yes", "good", "morning"]))  # ["hello", "morning"]