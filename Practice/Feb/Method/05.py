# 🔹 주어진 리스트에서 중복 요소를 제거하고, 내림차순 정렬한 후, 리스트를 다시 뒤집으세요.

values = [4, 2, 8, 4, 1, 9, 2, 8]

# 1) 중복 요소 제거
for value in values:
    if value in values:
        values.remove(value)
print(values)

# 2) 내림차순 정렬
values.sort(reverse= True)
print(values)

# 3) 리스트 뒤집기
values.sort()
print(values)
