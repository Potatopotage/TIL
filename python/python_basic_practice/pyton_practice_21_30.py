url = 'https://wikidocs.net/7022'

# 21

letters = 'python'

print(letters[1])
print(letters[3])

# 22

license_plate = '22가 2210'
print(license_plate[-4::1])

# 23

string = "홀짝홀짝홀짝"
print(string[::2])

# 24

string = "PYTHON"
print(string[::-1])

# 25

phone_number = '010-1111-2222'
phone_number = phone_number.replace('-', ' ')
print(phone_number)

# 26
phone_number = phone_number.replace(' ', '')
print(phone_number)

# 27

url = "http://sharebook.kr"
print(url[-2:])

# 28

lang = 'python'
# lang[0] = 'P'
# 문자열은 수정 불가능
print(lang)

# 29
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

# 30
string = 'abcd'
string.replace('b', 'B') #재할당 해야함!
print(string)