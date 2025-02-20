# book_id: 5자리 숫자여야 합니다.
# title: 비어있지 않아야 하며 100자를 초과하지 않아야 합니다.
# author: 비어있지 않아야 하며 50자를 초과하지 않아야 합니다.
# publication_year: 1900에서 현재 연도 사이의 4자리 숫자여야 합니다.
# is_available: True 또는 False여야 합니다.

book = {
    'book_id': '12345',
    'title': 'Python Programming',
    'author': 'John Doe',
    'publication_year': 2020,
    'is_available': True
}

from datetime import datetime

now = datetime.now()
year_now = str(now)[0:4]

# book의 각 요소를 검사하는 함수
def is_validation(book):

    global year_now

    false_list = []

    for key, value in book.items():
        if key == 'book' and len(value) != 5:
            false_list.append(key)
        elif key == 'title' and (len(value) == 0 or len(value) > 100):
            false_list.append(key)
        elif key == 'author' and (len(value) == 0 or len(value) >50):
            false_list.append(key)
        elif key == 'publication_year' and ((value <= 1900 or value >= int(year_now))):
            false_list.append(key)
        elif key == 'is_available' and (value != True and value != False):
            false_list.append(key)
    if len(false_list) == 0:
        return True, false_list
    else:
        return False, false_list
    
is_book = is_validation(book)

print(is_book)
