# 주어진 문장 속 단어 중에서 길이가 4 이상인 단어만 리스트로 추출하는 코드를 작성하시오.

sentence = "The quick brown fox jumps over the lazy dog"

# 출력 예시
# ['quick', 'brown', 'jumps', 'over', 'lazy']

sentence_split = sentence.split(' ')
print(sentence_split)

print(list([x for x in sentence_split if len(x) >= 4]))