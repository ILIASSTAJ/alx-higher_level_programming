#!/usr/bin/python3

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
active_users = {}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
    print(user)
    print(status)
    print(users)


