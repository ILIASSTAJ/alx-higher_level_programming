#!/usr/bin/python3
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
active_users = {}
for user, status in users.copy().items():
        if status == 'active':
            active_users[user] = status
        print(users)
        print(active_users)

