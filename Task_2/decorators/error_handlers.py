from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found!"
        except ValueError as e:
            if "Phone number must have exactly 10 digits." in str(e):
                return "Phone number must have exactly 10 digits."
            elif "Invalid date format. Use DD.MM.YYYY" in str(e):
                return "Invalid date format. Use DD.MM.YYYY"
            else:
                return "Give me name and phone please."
        except IndexError:
            return "Invalid input! Please provide correct data."

    return inner
