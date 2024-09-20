import matplotlib.pyplot as plt
from math import *
from decimal import Decimal, getcontext
import decimal
import sys
import mpmath

# Increase the maximum number of digits for int conversion
sys.set_int_max_str_digits(228505 + 1)  # +1 to ensure the given number is not too low

path='Calc-Start-Coordinate.txt'
direction=Decimal(input("Direction: If traverse down, input 1, traverse up -1 :"))
total_repetition=int(input("Total repetitions:"))
y=0
step=Decimal(750100./325)

decimal.getcontext().prec = 218510
mpmath.mp.dps = 220000

def calculate_number_of_digits(exponent):
    # Calculate the number of digits
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
    digits = calculate_number_of_digits(end)
    with open("Calc-Start-Coordinate-By-Integer.txt", "w") as file:
        file.write(f"{digits}")

def cal(n,b,y):
    with open("Deviatioin.txt", "r") as file:
        deviation = file.read().strip()
    with open("Term_For_Calc.txt", 'r') as file:
        start_coordinate_str = file.read().strip()
    if(start_coordinate_str): 
        print("Read Terminate-coordinate Success.")
    start_coordinate = mpmath.mpf(start_coordinate_str)

    start_coordinate = mpmath.mpf(start_coordinate) + mpmath.mpf(deviation)
    point=start_coordinate
    print("Calculating Start-Coordinate...")
    for _ in range(n):
        q=point+step
        next=point+b*step
        point=next 
        y=y+b*step
    return point
with open(path, "w") as file:
    file.write("")
end = cal(total_repetition,direction,y)
draw(end)
print("first point =>",f"2^{end}")