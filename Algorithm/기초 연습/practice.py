def test_pld(word):
    if len(word) % 2 == 0:
        if word[:int(len(word)/2)] == word[-1:-(int(len(word)/2 + 1)):-1]:
            print("True")
        else:
            print('False')
    elif len(word) % 2 == 1:
        if word[:int(len(word)//2)] == word[-1:-(int(len(word)//2 + 1)): - 1]:
            print('True')
        else:
            print("False")
    return word

test_pld('안녕하녕안')

