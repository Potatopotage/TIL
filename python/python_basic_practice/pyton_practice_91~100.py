url = 'https://wikidocs.net/78558'

# 91
inventory = {
    '메로나' : [300, 20],
    '비비빅' : [400, 3],
    '죠스바' : [250, 100]
}

print(inventory)

# 92
print(f'{inventory["메로나"][0]} 원')

# 93
print(f'{inventory["메로나"][1]} 개')

# 94
inventory['월드콘'] = [500, 7]
print(inventory)

# 95
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream_keys = []
icecream_keys = icecream.keys()
print(icecream_keys)

# 96
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream_value = icecream.values()
print(icecream_value)

# 97
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecrea_sum = sum(icecream.values())
print(icecrea_sum)

# 98
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}

icecream.update(new_product)
print(icecream)

# 99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

my_dict = dict(zip(keys, vals))
print(my_dict)

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

my_dict = dict(zip(date, close_price))
print(my_dict)