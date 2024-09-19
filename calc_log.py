import math
from decimal import Decimal, getcontext
import sys
# Increase precision of decimal operations
getcontext().prec = 300000


# Increase the maximum number of digits for int conversion
sys.set_int_max_str_digits(300000)  # +1 to ensure the given number is not too low

# Step 1: Convert the large integer to an exponent of 2 and coefficient
def integer_to_exp_and_coef(large_int):
    # Use Decimal for high precision
    large_int_decimal = Decimal(large_int)
    exponent = int(math.floor(math.log2(large_int_decimal)))
    coefficient = large_int_decimal / Decimal(2) ** exponent
    return coefficient, exponent

# Step 2: Reconvert the exponent and coefficient to the exact initial integer
def exp_and_coef_to_integer(coefficient, exponent):
    # Use Decimal for high precision reconstruction
    reconstructed_int = int(coefficient * (Decimal(2) ** exponent))
    return reconstructed_int

# Example:
# Generate a large integer with 280505 digits for demonstration purposes.
# Note: In practice, this would be your input integer.
large_int_str = '9' * 280505
large_int = int(large_int_str)

print(f"Initial Integer: {large_int}")

# Convert to coefficient and exponent
coefficient, exponent_of_2 = integer_to_exp_and_coef(large_int)
print(f"Coefficient: {coefficient}")
print(f"Exponent of 2: {exponent_of_2}")

# Reconstruct the original integer
reconstructed_int = exp_and_coef_to_integer(coefficient, exponent_of_2)
print(f"Reconstructed Integer: {reconstructed_int}")

# Verify equality
is_equal = large_int == reconstructed_int
print(f"Is equal: {is_equal}")

assert is_equal, "The reconstructed integer does not match the original integer!"
