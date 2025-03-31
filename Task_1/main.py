from collections import UserDict
from datetime import datetime, timedelta


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
        self.birthday = Birthday(birthday_date) if birthday_date else None

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name}, phones: {phones}, birthday: {self.birthday}"

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

    def add_birthday(self, birthday_date):
        self.birthday = Birthday(birthday_date)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        return self.data.pop(name)

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = datetime.now().date()
        end_date = today + timedelta(days=days)

        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if today <= birthday_this_year <= end_date:
                    upcoming_birthdays.append(record)

        return upcoming_birthdays


class Birthday(Field):
    def __init__(self, value):
        try:
            if self.validate(value):
                parse_date = datetime.strptime(value, "%d.%m.%Y").date()
                super().__init__(parse_date)
            else:
                raise ValueError("Value must be a non-empty string in DD.MM.YYY")

        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    @staticmethod
    def validate(value):
        return value is not None and isinstance(value, str)


# ========================================================

book = AddressBook()
# john_record = Record("John", "1988.10.10")
john_record = Record("John", "02.04.1988")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")


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
br = book.get_upcoming_birthdays()

for i in br:
    print(f"The next br in this weak  --- {i}")


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
