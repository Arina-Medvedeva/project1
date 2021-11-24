import json


class Person:

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __init__(self, name, birthday_age, phones):
        self.name = name
        self.birthday_age = birthday_age
        self.formatted_phones = phone

    name = ""
    birthday_age = ""
    formatted_phones = []