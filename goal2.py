import matplotlib.pyplot as plt
from math import *
import math
import os
from decimal import Decimal, getcontext

path='Calc-Start-Coordinate.txt'
a=float(input("Terminate point coordinate (e.g., for 2^400000 enter 400000):"))
b=float(input("Direction b = 1 or -1 :"))
n=int(input("Total repetitions:"))
y=0
p=750100./300
print(p)

def calculate_number_of_digits(exponent):
    # Calculate the number of digits
    num_digits = int(math.floor(exponent * math.log10(2))) + 1
    return num_digits

def calculate_large_power_digits(base, exponent):
     # Set precision high enough to handle the large number
    getcontext().prec = exponent

    # Calculate the large power
    result = Decimal(base) ** Decimal(exponent)

    return str(result)

def draw(end):
    with open(path, "w") as file:
        file.write(f"Start Coordinate From Terminate Coordinate: 2^{end}")
    digits = calculate_large_power_digits(2, int(end))
    with open("Calc-Start-Coordinate-By-Integer", "w") as file:
        file.write(f"Start Coordinate From Terminate Coordinate: {digits}")
def cal(a,n,b,y):
    point=a
    for _ in range(n):
        q=point+p
        next=point+b*p
        # draw(point, q, y)
        point=next 
        y=y+b*p
    return point
with open(path, "w") as file:
    file.write("")
end = cal(a,n,b,y)
draw(end)
print("first point =>",f"2^{end}")