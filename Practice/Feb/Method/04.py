# 🔹 문장에서 모든 공백을 제거하고, 모든 문자가 알파벳인지 확인한 후, 특정 단어를 다른 단어로 변경하세요.

sentence = " Data Science is amazing! "

# 1) 문자열 앞뒤 공백 제거
stripted_sentece = sentence.strip(' ')
print(stripted_sentece)

# 2) 문자열이 모두 알파벳인지 확인
print(stripted_sentece.isalpha())


# 3) 'Science'를 'Analysis'로 변경
changed_sentence = stripted_sentece.replace('Science', "Analysis")
print(changed_sentence)