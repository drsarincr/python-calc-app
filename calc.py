def power_of(base, exponent):
    return base * exponent  # BUG: 2 to the power of 3 should be 8, but this returns 6!

print("2 to the power of 3:", power_of(2, 3))