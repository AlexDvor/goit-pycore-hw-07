from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise ValueError("Phone number must have exactly 10 digits.")

    @staticmethod
    def validate(value):
        return value.isdigit() and len(value) == 10


class Record:

    def __init__(self, name, birthday_date=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday_date)

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                self.phones.remove(p)
                self.add_phone(new_phone)
                return True
        return False

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        return self.data.pop(name)


class Birthday(Field):
    def __init__(self, value):
        if value is None or not isinstance(value, str):
            return
        try:
            parse = datetime.strptime(value, "%d.%m.%Y").date()
            print(f"date ------ {parse}")

        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


# class Record:
#     def __init__(self, name):
#         self.name = Name(name)
#         self.phones = []
#         self.birthday = None


# ========================================================

book = AddressBook()
# john_record = Record("John", "1988.10.10")
john_record = Record("John", "10.10.1988")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
print(f"John_record :{john_record}")
book.add_record(john_record)
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")
book.delete("Jane")


"""
По перше додамо додатковий функціонал до класів з попередньої домашньої роботи:

Додайте поле birthday для дня народження в клас Record . Це поле має бути класу Birthday. Це поле не обов'язкове, але може бути тільки одне.
class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

Додайте функціонал роботи з Birthday у клас Record, а саме функцію add_birthday, яка додає день народження до контакту.
Додайте функціонал перевірки на правильність наведених значень для полів Phone, Birthday.
Додайте та адаптуйте до класу AddressBook нашу функцію з четвертого домашнього завдання, тиждень 3, get_upcoming_birthdays, яка для контактів адресної книги повертає список користувачів, яких потрібно привітати по днях на наступному тижні.


Тепер ваш бот повинен працювати саме з функціоналом класу AddressBook. Це значить, що замість словника contacts ми використовуємо book = AddressBook()




"""
