def parse_input(inputted_data: str):
    command = inputted_data.split()
    command = [word.lower().strip() for word in command]
    return command
