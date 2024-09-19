import math
import sys
import mpmath
# Set precision high enough
mpmath.mp.dps = 218510  # Extra digits for safety margin


# Increase the maximum number of digits for int conversion
sys.set_int_max_str_digits(228505 + 1)  # +1 to ensure the given number is not too low

def int_to_exponent_of_2(n):
    """
    Converts an integer n to the exponent representation of 2 (i.e., finds e such that n ≈ 2^e).
    
    Note: This function assumes n is a power of 2 for exact conversion.
    """
    if n <= 0:
        raise ValueError("The input must be a positive integer.")
    # Calculate the exponent
    e = math.log2(n)
    
    # Verify if n is exactly a power of 2
    if 2 ** int(e) != n:
        raise ValueError(f"The number {n} is not an exact power of 2.")
    
    return int(e)

def exponent_of_2_to_int(e):
    """
    Converts an exponent e back to the original integer in the form of 2^e.
    """
    # Compute the power of 2 to the given exponent
    result = mpmath.power(2, e)

    # Convert the result to string and remove any scientific notation
    result_str = mpmath.nstr(result, mpmath.mp.dps, strip_zeros=False)

    print(result_str)

# Example usage
large_int = 2 ** 725854.9729681012836942647540
# Convert integer to exponent
exp = int_to_exponent_of_2(large_int)
print(f"Exponent: {exp}")  # Output should be 750100

# Reverse calculation: exponent back to integer
reconstructed_int = exponent_of_2_to_int(exp)
with open("test.txt", "w") as file:
        file.write(f"integer for large number: {reconstructed_int}")
print(f"Reconstructed Integer: {reconstructed_int}")

# Check if the numbers are the same
print(f"Validation: {large_int == reconstructed_int}")  # Output should be True
