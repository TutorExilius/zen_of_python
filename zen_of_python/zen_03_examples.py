"""Zen 3: Simple is better than complex."""


# ------------ Example 1 ------------

# count non alpha characters

"""complex"""
def count_non_alpha(text: str) -> int:
    return len(re.findall(r'^[^a-zA-Z]', s))

"""simple"""
def count_non_alpha(text: str) -> int:
    non_alpha_counter = 0

    for char in text:
        if not char.isalpha():
            non_alpha_counter += 1

    return non_alpha_counter