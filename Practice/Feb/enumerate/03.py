# enumerate를 사용하여 짝수 인덱스에 있는 단어만 출력하는 코드를 작성하세요.

words = ["hello", "python", "enumerate", "function"]

for index, word in enumerate(words):
    if index % 2 == 0:
        print(word)
        