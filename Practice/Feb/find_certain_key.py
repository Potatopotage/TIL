# 딕셔너리와 키가 주어졌을 때, 해당 키가 존재하면 True를 반환하고, 
# 존재하지 않으면 False를 반환하는 함수를 작성하세요.

def key_exists(dictionary, key):
    # dictionary의 key로 이루어진 리스트 생성
    dictionary_keys = list(dictionary.keys())
    if key in dictionary_keys:
        return True
    else:
        return False


print(key_exists({'name': 'Alice', 'age': 25}, 'name')) # True
print(key_exists({'name': 'Alice', 'age': 25}, 'gender')) # False
print(key_exists({}, 'anything')) # False

