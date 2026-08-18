import math

def change_base(value, initial_base, final_base):

    new_value = 0

        
    for digit in str(value):
         new_value = new_value * initial_base + int(digit)

        
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


