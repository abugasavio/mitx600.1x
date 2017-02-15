def closest_power(base, num):
    """
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    """
    exponential = 0

    while (base ** exponential) <= num:
        exponential += 1

    before = base ** (exponential - 1)
    after = base ** exponential

    if abs(before - num) == abs(after - num):
        return exponential - 1
    elif abs(before - num) < abs(after - num):
        return exponential - 1
    else:
        return exponential

print(closest_power(4, 62))





