"""Zen 4: Complex is better than complicated."""


# ------------ Example 1 ------------

# count non alpha characters

"""complicated"""
def count_non_alpha(text: str) -> int:
    alpha = "abcdefghijklmnopqrstuvwxyz"
    non_alpha_text = []

    for char in text:
        is_non_alpha = False

        try:
            if char.lower() not in alpha:
                is_non_alpha = True
        except:  # catch None etc. or any mismatched and count them as non-ascii
            is_non_alpha = True

        if is_non_alpha:
            non_alpha_text.append(char)

    return len(non_alpha_text)

"""complex"""
def count_non_alpha(text: str) -> int:
    return len(re.findall(r'^[^a-zA-Z]', s))
