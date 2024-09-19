import matplotlib.pyplot as plt
from math import *
import math
import os
from decimal import Decimal, getcontext
import decimal
import sys
import mpmath

# Increase the maximum number of digits for int conversion
sys.set_int_max_str_digits(228505 + 1)  # +1 to ensure the given number is not too low

path='Calc-Start-Coordinate.txt'
# a=Decimal(input("Terminate point coordinate (e.g., for 2^400000 enter 400000):"))
b=Decimal(input("Direction b = 1 or -1 :"))
n=int(input("Total repetitions:"))
y=0
p=Decimal(750100./325)
print("p", p)

decimal.getcontext().prec = 218510
mpmath.mp.dps = 218510

def calculate_number_of_digits(exponent):
    # Calculate the number of digits
    # num_digits = int(math.floor(exponent * math.log10(2))) + 1
    
    # exponent = decimal.Decimal(exponent)
    print("exponent", exponent)

    result = mpmath.power(2, exponent)

    # Convert the result to string and remove any scientific notation
    result_str = mpmath.nstr(result, mpmath.mp.dps, strip_zeros=False)
    # print(result_str)
    return result_str

def calculate_large_power_digits(base, exponent):
     # Set precision high enough to handle the large number
    getcontext().prec = exponent

    # Calculate the large power
    result = Decimal(base) ** Decimal(exponent)

    return str(result)

def exp_and_coef_to_integer(coefficient, exponent):
    # Use Decimal for high precision reconstruction
    if isinstance(coefficient, str):
        coefficient = Decimal(coefficient)
    # Use Decimal for high precision reconstruction
    reconstructed_int = int(coefficient * (Decimal(2) ** exponent))
    return reconstructed_int

def draw(end):
    with open(path, "w") as file:
        file.write(f"Start Coordinate From Terminate Coordinate: 2^{end}")
    # digits = calculate_large_power_digits(2, end)
    # digits = exp_and_coef_to_integer("1.962874727075156462132929369",end)
    digits = calculate_number_of_digits(end)
    with open("Calc-Start-Coordinate-By-Integer.txt", "w") as file:
        file.write(f"{digits}")
def cal(n,b,y):
    with open("Terminate-coordinate.txt", 'r') as file:
        start_coordinate_str = file.read().strip()
    if(start_coordinate_str): 
        print("Read Terminate-coordinate Success.")
    start_coordinate = mpmath.mpf(start_coordinate_str)
    print("Terminate coordinate", start_coordinate)
    point=start_coordinate
    for _ in range(n):
        q=point+p
        next=point+b*p
        # draw(point, q, y)
        point=next 
        y=y+b*p
    return point
with open(path, "w") as file:
    file.write("")
end = cal(n,b,y)
draw(end)
print("first point =>",f"2^{end}")