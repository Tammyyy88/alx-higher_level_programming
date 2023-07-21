#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8)
    Args:
        filename (str): The name of the file to append.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        current_position = file.tell()  # Get the current position (end of the file)
        file.write(text)
        file.seek(0, 2)  # Move the cursor to the end of the file
        return file.tell() - current_position
