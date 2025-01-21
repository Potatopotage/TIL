url = 'https://wikidocs.net/78558'

# 71
my_variable = ()

# 72
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')

# 73
my_tuple = (1,)

# 74
# 튜플은 변경 불가능!

# 75
t = 1, 2, 3, 4
print(type(t))
# 괄호 없이도 동작

# 76
t = ('a', 'b', 'c')
t = list(t)
t[0] = 'A'
t[1] = 'B'
t[2] = 'C'
t = tuple(t)
print(t)

# 77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)

# 78
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = tuple(interest)

# 79
# pass

# 80
number = tuple(range(2, 100, 2))
print(number)