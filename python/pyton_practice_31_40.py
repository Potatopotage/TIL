url = 'https://wikidocs.net/7024'

# 31

a = '3'
b = '4'
print(a+b)

# 32

print('HI'*3)

# 33
print('-'*80)

# 34
t1 = 'python'
t2 = 'java'
result_t = t1 + " " + t2 + ' '
print(result_t*3)

# 35

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print('이름: %s 나이: %d' %(name1, age1))
print('이름: %s 나이: %d' %(name2, age2))

# 36

print('이름: {} 나이: {}' .format(name1, age1))
print('이름: {} 나이: {}' .format(name2, age2))

# 37

print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

# 38

상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(',', '')
상장주식수 = int(상장주식수)
print(상장주식수)

# 39

분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 40

data = "   삼성전자    "
data = data.strip()
print(data)