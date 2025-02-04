# enumerate 함수를 사용하여 "0: 사과", "1: 바나나" 와 같은 형식으로 출력하는 코드를 작성하세요.

fruits = ["사과", "바나나", "딸기", "포도"]

for index, fruit in enumerate(fruits):
    print(f'{index}: {fruit}')