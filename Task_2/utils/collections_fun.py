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
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if not record:
        return "Contact not found!"

    if record.edit_phone(old_phone, new_phone):
        return f"Contact {name} updated with new phone!"
    return "Old phone number not found!"


@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found!"

    phones = [p.value for p in record.phones]
    return (
        f"Phone(s) for {name}: {', '.join(phones)}"
        if phones
        else "No phone number found!"
    )


@input_error
def show_all(_, book: AddressBook):
    if not book.data:
        return "Your address book is empty!"

    return "\n".join([str(record) for record in book.data.values()])


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday_date = args
    record = book.find(name)
    if not record:
        return "Contact not found!"

    record.add_birthday(birthday_date)
    return f"Birthday for {name} added!"


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        return "Contact not found!"

    if not record.birthday:
        return f"No birthday found for {name}"

    return f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"


@input_error
def birthdays(_, book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays == "No upcoming birthdays.":
        return upcoming_birthdays

    return "\n".join(
        [
            f"{record.name.value}: {record.birthday.value.strftime('%d.%m.%Y')}"
            for record in upcoming_birthdays
        ]
    )
