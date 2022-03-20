"""Zen 2: Explicit is better than implicit."""


# ------------ Example 1 ------------

# check if list is none_or_empty

my_list = []

"""implicit"""
def is_none_or_empty(my_list: list) -> bool:
    return not my_list

"""explicit"""
def is_none_or_empty(my_list: list) -> bool:
    return not bool(my_list)
    "or"
    return my_list is None or len(my_list) == 0

print(check_none_or_empty(my_list))