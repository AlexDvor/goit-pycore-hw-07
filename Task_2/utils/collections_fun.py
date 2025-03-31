from decorators.error_handlers import input_error
from models.address_book import AddressBook
from models.record import Record


@input_error
def add_contact(args, book: AddressBook):

    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, contacts: dict):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated!"
    else:
        raise KeyError


@input_error
def show_phone(args, contacts: dict):
    if not contacts:
        return "Contact list is empty!"

    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        raise KeyError


@input_error
def show_all(_, contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "Your list is empty!"


def add_birthday(args, book: AddressBook):
    name, birthday_date = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday_date)
        return f"Birthday for {name} added!"
    else:
        return "Contact not found!"


def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}"
    return "Contact not found or birthday not set!"


def birthdays(_, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays this week."
    return "\n".join(
        [
            f"{rec.name.value}: {rec.birthday.value.strftime('%d.%m.%Y')}"
            for rec in upcoming
        ]
    )
