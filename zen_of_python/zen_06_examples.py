"""Zen 6: Sparse is better than dense."""

# enter persons first and last name and say hello to that person

"""dense"""
def say_hello():
    first_name = None
    last_name = None

    while not first_name:
        first_name = input("Your first name:")

    while not last_name:
        last_name = input("Your last name:")

    full_name = first_name + " " + last_name
    print("Hello", full_name)

"""sparse"""
def input_name(prompt_message: str) -> str:
    name = None

    while not name:
        name = input(prompt_message)

    return name

def get_first_name() -> str:
    first_name = input_name("Your first name:")
    return first_name

def get_last_name() -> str:
    last_name = input_name("Your last name:")
    return last_name

def say_hello():
    first_name = get_first_name()
    last_name = get_last_name()

    full_name = first_name + " " + last_name
    print("Hello", full_name)
