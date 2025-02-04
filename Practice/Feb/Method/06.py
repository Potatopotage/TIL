# 🔹 딕셔너리에서 특정 키의 값을 가져오고, 해당 키를 제거한 후, 딕셔너리를 초기화하세요.

user_info = {"username": "john_doe", "email": "john@example.com", "age": 30}

# 1) 'email' 키의 값을 가져오기 (키가 없으면 'Not Found' 반환)
email_value = user_info.get('email', 'Not Found')
print(email_value)

# 2) 'age' 키를 제거
user_info.pop('age')
print(user_info)


# 3) 딕셔너리를 초기화 (모든 값 삭제)
user_info.clear()
print(user_info)
