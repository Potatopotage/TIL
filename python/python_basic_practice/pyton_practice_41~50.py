url = 'https://wikidocs.net/78558'

# 41

ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)

# 42

ticker = ticker.lower()
print(ticker)

# 43

word = 'hello'
word = word.upper()
print(word)

# 44
file_name = "보고서.xlsx"
file_name = file_name.endswith('xlsx')
print(file_name)

# 45

file_name = "보고서.xlsx"
file_name_xlsx = file_name.endswith('xlsx')
file_name_xls = file_name.endswith('xls')

if file_name_xlsx == True:
    print('xlsx 또는 xls로 끝납니다')
elif file_name_xls == True:
    print('xlsx 또는 xls로 끝납니다')
else:
    print('xlsx 또는 xls로 끝나지 않습니다')

# 46

