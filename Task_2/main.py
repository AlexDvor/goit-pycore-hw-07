from models.address_book import AddressBook
from utils import collections_fun as fn
from utils.parse_input import parse_input


def main():
    book = AddressBook()
    print(f"book ------ {book}")
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        if not user_input:
            print("Invalid command.")
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(fn.add_contact(args, book))
        elif command == "change":
            print(fn.change_contact(args, book))
        elif command == "phone":
            print(fn.show_phone(args, book))
        elif command == "all":
            print(fn.show_all(args, book))
        elif command == "add-birthday":
            print(fn.add_birthday(args, book))
        elif command == "show-birthday":
            print(fn.show_birthday(args, book))
        elif command == "birthdays":
            print(fn.birthdays(args, book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
