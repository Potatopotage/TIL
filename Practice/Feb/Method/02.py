# 🔹 리스트에 새로운 요소를 추가하고, 중복된 값의 개수를 확인한 후, 가장 마지막에 추가된 요소를 제거하세요.

numbers = [1, 2, 3, 4, 5, 3, 2, 1]

# 1) 리스트에 3을 추가
numbers.append(3)

# 2) 리스트에서 3의 개수 세기
count3 = numbers.count(3)
print(count3)

# 3) 리스트의 마지막 요소 제거
numbers.pop()
print(numbers)
