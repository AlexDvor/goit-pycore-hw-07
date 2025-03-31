from models.field import Field
from datetime import datetime


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


def parse_input(inputted_data: str):
    command = inputted_data.split()
    command = [word.lower().strip() for word in command]
    return command
