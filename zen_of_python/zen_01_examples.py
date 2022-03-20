"""Zen 1: Beautiful is better than ugly."""


# ------------ Example 1 ------------

# print only even numbers

numbers = [9, 3, 2, 12, 4, 33, 42, 11, 7, 5, 8]

"""ugly"""
for i in range(0, len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i])

"""beautiful"""
for num in numbers:
    if num % 2 == 0:
        print(num)
