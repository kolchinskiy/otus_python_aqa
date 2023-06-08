import json
from csv import DictReader

new_list = []
new_list_books = []

with open('books.csv', "r") as f:
    reader = list(DictReader(f))
    for book in reader:
        book_keys = ['title', 'author', 'pages', 'genre']
        book_values = [book['Title'], book['Author'], book['Pages'], book['Genre']]
        next_book = dict(list(zip(book_keys, book_values)))
        new_list_books.append(next_book)


with open('users.json', "r") as f1:
    users = json.load(f1)
    x = len(reader) // len(users) + 1     # по столько книг достанется везунчикам
    vez = len(reader) % len(users)        # количество везунчиков
    start = 0
    user_number = 0
    for user in users:
        user_number += 1
        finish = start + x
        if user_number == vez:
            x -= 1         # везунчики закончились, теперь раздаём меньше книг
        user_keys = ['name', 'gender', 'address', 'age', 'books']
        user_values = [user['name'], user['gender'], user['address'], user['age'], new_list_books[start:finish]]
        next_user = dict(list(zip(user_keys, user_values)))
        new_list.append(next_user)
        start = finish

with open('result.json', "w") as f2:
    s = json.dumps(new_list, indent=4)
    f2.write(s)
