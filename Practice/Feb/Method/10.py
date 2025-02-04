# 🔹 딕셔너리를 다른 딕셔너리 값으로 갱신하고, 특정 키의 값을 기본값으로 설정한 후, 모든 키를 리스트로 변환하세요.

person = {"name": "Alice", "age": 25}
new_info = {"age": 26, "city": "New York"}

# 1) person 딕셔너리를 new_info 값으로 갱신
person.update(new_info)
print(person)

# 2) 'gender' 키를 기본값 'Unknown'으로 설정
gender = person.setdefault('gender', "UnKown")
print(gender)

# 3) 모든 키를 리스트로 변환
key_list = person.keys()
print(key_list)