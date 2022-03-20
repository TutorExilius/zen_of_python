"""Zen 7: Readability counts."""


# ------------ Example 1 ------------

# check if list is none_or_empty

my_list = []

"""not very readable"""
def is_none_or_empty(my_list: list) -> bool:
    return not my_list

"""readable"""
def is_none_or_empty(my_list: list) -> bool:
    return my_list is None or len(my_list) == 0

print(check_none_or_empty(my_list))