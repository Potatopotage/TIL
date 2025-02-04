# 🔹 리스트에 여러 개의 요소를 한 번에 추가하고, 특정 요소를 삭제한 후, 리스트에서 특정 요소의 위치를 찾으세요.

fruits = ["apple", "banana", "cherry"]

# 1) 리스트에 ["mango", "grape"] 추가
fruits.extend(['mango', 'grape'])
print(fruits)

# 2) "banana" 삭제
fruits.remove('banana')
print(fruits)

# 3) "cherry"의 인덱스 찾기
cherry_index = fruits.index('cherry')
print(cherry_index)
