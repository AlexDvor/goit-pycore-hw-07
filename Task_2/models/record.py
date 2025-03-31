from models.name import Name
from models.phone import Phone
from models.birthday import Birthday


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
