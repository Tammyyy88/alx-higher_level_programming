#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout

    Args:
        filename (str): Name of the text file to be read

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')


if __name__ == '__main__':
    read_file("my_file_0.txt")
