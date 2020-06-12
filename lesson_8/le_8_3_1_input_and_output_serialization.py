import json


users = [
    {
        'username': 'john',
        'email': 'john@hotmail.com'
    },
    {
        'username': 'linda',
        'email': 'linda@hotmail.com'
    },
    {
        'username': 'mario',
        'email': 'mario@hotmail.com'
    },
]


class User:
    def __init__(self, name, email):
        self.username = name
        self.email = email

    def to_json(self):
        return {'username': self.username, 'email': self.email}


users = [User('John', 'john@hotmail.com'), User(name='Jane', email='jane@hotmail.com')]

with open('le_8_dir/example8_1.json', 'w') as file:
    json.dump(users, file, indent=2, default=User.to_json)
