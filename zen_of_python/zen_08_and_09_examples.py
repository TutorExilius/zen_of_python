"""Zen 8: Special cases aren't special enough to break the rules."""
"""Zen 9: Although practicality beats purity."""


# ------------ Example 1 ------------

# enter a number and make sure it is a integer

"""try to comply zen 7: 'Readability counts.'"""
def enter_a_number() -> int:
    while True:
        number = input("Enter a number:")

        if number.isdigit():
            return int(number)

"""break some ZENs, because of practicality"""
def enter_a_number() -> int:
    while True:
        try:
            return int(input("Enter a number:"))
        except:
            pass
