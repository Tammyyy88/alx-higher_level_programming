#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
  """
  Prints My name is <first name> <last name>

  Args:
    first_name: The first name.
    last_name: The last name. Defaults to "".

  Raises:
    TypeError: If first_name or last_name is not a string.
  """

  if not isinstance(first_name, str):
    raise TypeError("first_name must be a string")

  if not isinstance(last_name, str):
    last_name = ""

  print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
  say_my_name("John", "Smith")
  say_my_name("Walter", "White")
  say_my_name("Bob")
  try:
    say_my_name(12, "White")
  except Exception as e:
    print(e)
