
from datetime import date
from dateutil import relativedelta as rdelta
import json
from Helper import Helper
from Person import Person

json_book = []
people = []
with open("book.txt", "r", encoding="utf-8") as f:
    json_book = json.load(f)
    for contact in json_book:
        ob_python_json = json.loads(contact)
        name = ob_python_json['name']
        birthday_age = ob_python_json['birthday_age']
        phones = ob_python_json['formatted_phones']

        person = Person(name=name, birthday_age=birthday_age, phones=phones)
        people.append(person)

while True:
    comand = int(input('\n Введите 0, если хотите выйти из программы. \nВведите 1, если хотите отобразить весь список контактов. \nВведите 2, если хотите добавить новый контакт: '))

    if comand == 0:
        for item in people:
            Helper.correct_print(item)
            json_book.append(item.toJson())

        with open("book.txt", 'w', encoding='utf-8') as write_file:
            json.dump(json_book, write_file)
        break

    if comand == 1:
        for item in people:
            Helper.correct_print(item)

    if comand == 2:
        name = input("Введите ФИО: ")

        date_input = input("Введите дату рождения: ")
        date_elements = date_input.split(".")
        day = int(date_elements[0])
        month = int(date_elements[1])
        year = int(date_elements[2])
        birth_date = date(year, month, day)
        today = date.today()
        date_delta = rdelta.relativedelta(today, birth_date)
        yaers = str(date_delta.years)
        birthday_age = (date_input + " - " + yaers)

        n = int(input("Введите количество номеров телефонов: "))
        phones = []

        for i in range(n):
            current_phone = str(input("Введите телефон: "))
            phones.append(current_phone)

        cleared_phones = []
        for phone in phones:
            for letter in phone:
                if not letter.isdigit():
                    phone = phone.replace(letter, "")
            cleared_phones.append(phone)

        phones = []
        for phone in cleared_phones:
            phones.append(Helper.format_phone(phone))

        person = Person(name=name, birthday_age=birthday_age, phones=phones)


        people.append(person)