import json


class User:
    def __init__(self, name, email):
        self.username = name
        self.email = email

    def to_json(self):
        return {'username': self.username, 'email': self.email}

    @classmethod
    def from_json(cls, js_object):
        return cls(js_object['username'], js_object['email'])

    def __repr__(self):
        return f'User({self.username}, {self.email})'


def main():
    with open('le_8_dir/example8_1.json') as data:
        users = data.read()

    with open('le_8_dir/example8_1.json') as data:
        users = json.load(data)

    # print(users)
    with open('le_8_dir/example8_1.json') as data:
        users = json.load(data, object_hook=User.from_json)

    print(users)


if __name__ == '__main__':
    main()
    # tim = User('tim', 'tim@mail.com')
    # print(tim)
    j_str = json.dumps({'first_field': True, 'second_field': False, 'third_field': None, 'forth_field': User('tim', 'tim@mail.com').to_json()})
    print(type(j_str))
    print(j_str)
    print("------------------------------")
    j_dict = json.loads(j_str)
    print(type(j_dict))
    print(j_dict)

