# 🔹 주어진 문자열에서 모든 소문자를 대문자로 변환하고, 특정 단어가 첫 번째로 등장하는 위치를 찾으세요.
# 🔹 이후 해당 단어를 다른 단어로 변경하세요.

text = "Python is fun, but learning Python can be challenging."

# 1) 모든 문자를 대문자로 변환
# 2) 'PYTHON'이 처음 등장하는 위치 찾기
# 3) 'PYTHON'을 'JAVA'로 변경하기

# 결과: 'JAVA IS FUN, BUT LEARNING JAVA CAN BE CHALLENGING.'

# 모든 문자를 대문자로 변환
upper_text = text.upper()
print(upper_text)

# 'PYTHON'이 처음 등장하는 위치 찾기

python_index = upper_text.index('IS')
print(python_index)

# 'PYTHON'을 자바로 변경하기
changed_text = upper_text.replace('PYTHON', 'JAVA')
print(changed_text)