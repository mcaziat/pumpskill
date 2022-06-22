account1 = {'login': 'Ivan', 'password': 'q1'}
account2 = {'login': 'Petr', 'password': 'q2'}
account3 = {'login': 'Olga', 'password': 'q3'}
account4 = {'login': 'Anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

user_list = [user1, user2, user3, user4]

search = input('Введите ключ (name или account): ').lower()

try:
    count = 0
    for user in user_list:    
        print(f'Значение ключа {search} для юзера {count+1} = {user[search]}')
        count += 1

except KeyError:
    print('Введенный ключ не найден')

n = int(input('Введите порядковый номер: '))
print(f'Данные по юзеру {n}')

search_user = user_list[n-1]

print(f"Имя: {search_user['name']}")
print(f"Возраст: {search_user['age']}")
print(f"Логин: {search_user['account']['login']}")
print(f"Пароль: {search_user['account']['password']}")

move_user = int(input('Какого юзера переместить в конце: '))

user_list[move_user - 1], user_list[-1] = user_list[-1], user_list[move_user - 1]

print(user_list)

old = 0
for user in user_list:
    old += user['age']

print(old / len(user_list))
