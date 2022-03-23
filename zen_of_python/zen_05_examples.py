"""Zen 5: Flat is better than nested."""


# ------------ Example 1 ------------

# check if full aged and has valid vip pass

"""nested"""
def allowed_vip_access(age: int, valid_vip_pass: bool) -> bool:
    if age >= 18:
        if valid_vip_pass:
            return True
        else:
            return False
    else:
        return False

"""flat"""
def allowed_vip_access(age: int, valid_vip_pass: bool) -> bool:
    if age >= 18 and valid_vip_pass:
        return True

    return False

"""flat"""
def allowed_vip_access(age: int, valid_vip_pass: bool) -> bool:
    return age >= 18 and valid_vip_pass