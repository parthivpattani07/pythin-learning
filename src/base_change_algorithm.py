import math

def change_base(value, initial_base, final_base):
    if initial_base == 10:
        y = ""

        while value > 0:
            x = math.floor(value / final_base)
            r = value - final_base * x
            y = str(r) + y
            value = x

        return y if y else "0"

    else:
        new_value = 0

        # Convert initial base → base 10
        for digit in str(value):
            new_value = new_value * initial_base + int(digit)

        # Convert base 10 → final base
        y = ""
        while new_value > 0:
            x = math.floor(new_value / final_base)
            r = new_value - final_base * x
            y = str(r) + y
            new_value = x

        return y if y else "0"

"""
input:
print(change_base(500,7,8))

output:
365
"""


