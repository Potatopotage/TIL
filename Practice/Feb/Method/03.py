# 🔹 딕셔너리에 새로운 키를 추가하고, 특정 키의 값을 변경한 후, 모든 키와 값을 출력하세요.

student = {"name": "Alice", "age": 20, "major": "Computer Science"}

# 1) 새로운 키 'GPA'를 추가하고 기본값 3.5 설정
# student.setdefault('GPA')
# student['GPA'] = 3.5
# print(student)

student.update({'GPA': 3.5})
print(student)

# 2) 'age' 값을 21로 변경
student.update({'age': 21})
print(student)

# 3) 모든 키와 값을 튜플 형태로 출력
result = []

for key, value in student.items():
    result.append(key)
    result.append(value)

print(tuple(result))
