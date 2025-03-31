from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found!"
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid input! Please provide correct data."

    return inner
