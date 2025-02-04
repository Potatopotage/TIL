# 🔹 리스트의 모든 단어를 대문자로 변환하고, 하나의 문자열로 결합한 후, 단어 개수를 출력하세요.

words = ["hello", "world", "python", "rocks"]

# 1) 모든 단어를 대문자로 변환
word_list = []
for word in words:
    upper_word = word.upper()
    word_list.append(upper_word)

print(word_list)

# 2) 단어들을 하나의 문자열로 결합 (공백으로 구분)
result = ' '.join(word_list)
print(result)

# 3) 단어 개수 출력

word_number = result.count(' ')
word_final_number = word_number + 1
print(word_final_number)

