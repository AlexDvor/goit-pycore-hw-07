from decorators.error_handlers import input_error


@input_error
def add_contact(args, contacts: dict):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added!"


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
