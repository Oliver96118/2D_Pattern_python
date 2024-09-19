import numpy as np
import json
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext
from math import *
import sys
from mpmath import mp, log

path = []
polygons = []
step = mp.mpf(750100./325)

# Set the precision (number of decimal places)
mp.dps = 218506

# Log scaling function for large numbers
def log_scale(value):
    if value <= 0:
        return 0
    return log(value)

# Function to round an mpf number to a specific number of decimal places
def round_mpf(number, decimal_places):
    rounded_str = mp.nstr(number, decimal_places + 1)
    return mp.mpf(rounded_str)

# Function for reading start-coordinate.txt
def calculate_exponent(file_path):
    try:
        with open(file_path, 'r') as file:
            start_coordinate_str = file.read().strip()
        
        # Increase the maximum number of digits for int conversion
        sys.set_int_max_str_digits(218505 + 1)  # +1 to ensure the given number is not too low
        
        # Input start coordinate
        start_coordinate = int(start_coordinate_str)
        
        # Covert start coordinate to a high-precision floating-point number
        start_coordinate = mp.mpf(start_coordinate)
        
        # Verify start coordinate
        if start_coordinate <= 0:
            raise ValueError("The number must be positive.")

        # Calculate the exponent
        exponent = log(start_coordinate, 2)

        # Verify if start_coordinate exactly a power of 2
        if 2 ** exponent != start_coordinate:
            print("The x-coordinate of start point is not an exact power of 2. So an accuracy may be a little down.")
        else:
            print("The x-coordinate of start point is an exact power of 2.")
        
        return exponent
    
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

def calculate_number_of_digits(exponent):
    # Calculate the number of digits
    print("exponent", exponent)

    result = mp.power(2, exponent)

    # Convert the result to string and remove any scientific notation
    result_str = mp.nstr(result, mp.dps, strip_zeros=False)
    # print(result_str)
    return result_str

# Function to draw the triangle
def draw_triangle(vertices, ax):
    polygon = plt.Polygon(vertices, fill='darkblue', edgecolor='black')
    ax.add_patch(polygon)

# Function to draw vertical lines
def draw_vertical_lines(x_coords, y_min, y_max, color, ax):
    for x in x_coords:
        ax.plot([x, x], [y_min, y_max], color=color)

# Function to traverse upward
def traverse_top(a,c1,c2,y,ax):
    print("travese_top")
    point=a
    print("step", step)
    n = 0
    while(point<c2):
        n = n + 1
        next = point + step
        point=next 
        y = y + step
        path.append({"shape": "triangle", "equation": [f"x=2^{point}", "y=1", f"2^{y}*x+(2^{point}-2^{next})*y=2^({y}+{next})"]})
        if(point + step > c2):
           path.append("Terminate Point coordinate: 2^{}\n".format(next))
           path.append("Total repetitions: {}".format(n))
           write_json(path)
           with open("Terminate-coordinate-exponent.txt", "w") as file:
                # file.write(f"Terminate Point coordinate: (2^{next}, 1)")
                file.write(f"{calculate_number_of_digits(next)}")

# Function to traverse downward
def traverse_down(start_point_x,c1,c2,y,ax):
    print('traverse_down')
    point = start_point_x
    n=0
    while(point>c1):
        n = n + 1
        next= point - step
        point=next
        y = y - step
        path.append({"shape": "triangle", "equation": [f"x=2^{round_mpf(point, 10)}", "y=1", f"2^{y}*x+(2^{round_mpf(point, 10)}-2^{round_mpf(next, 10)})*y=2^({y}+{round_mpf(next, 10)})"]})
        # polygons.append({ "p1" : (log_scale(2 ** point), 1), 'p2': (log_scale(2 ** next), 1), 'p3': (log_scale(2 ** point), log_scale(2 ** y))})
        if(point - step < c1):
            path.append("Terminate Point coordinate: 2^{}\n".format(next))
            path.append("Total repetitions: {}".format(n))
            write_json(path)
            with open("Terminate-coordinate-exponent.txt", "w") as file:
                file.write(f"{next}")
            with open("Terminate-coordinate-integer.txt", "w") as file:
                file.write(f"{calculate_number_of_digits(next)}")

        #    draw_polygon(polygons, ax)

# def draw_polygon(polygons, ax):

#     for vertices in polygons:
#         polygon = plt.Polygon([vertices['p1'], vertices['p2'], vertices['p3']], fill='darkblue', edgecolor='black')
#         ax.add_patch(polygon)
   
    # with open(path, "a") as file:
    #     file.write(f"x=2^{x1}\n y=1\n 2^{y}*x+(2^{x1}-2^{x2})*y=2^({y}+{x2})\n")

def write_json(path):
    json_data = json.dumps(path, indent=4, default=str)
    with open('pattern.json', 'w') as json_file:
        json_file.write(json_data)

def main():

    with open('pattern.json', "w") as file:
        file.write("")

    # Input vertices for the triangle
    # print("Enter the vertices of the triangle (format: x,y):")
    # v1 = tuple(map(int, input("Exponent for Vertex 1 (e.g., for 2^500000 enter 500000): ").split(',')))
    # v2 = tuple(map(int, input("Exponent for Vertex 2 (e.g., for 2^500000 enter 500000): ").split(',')))
    # v3 = tuple(map(int, input("Exponent for Vertex 3 (e.g., for 2^500000 enter 500000): ").split(',')))
    v1 = (0,0)
    v2 = (750000, 0)
    v3 = (750000, 750000)

    vertices = [(log_scale(2 ** v1[0]), log_scale(2 ** v1[1])), 
                (log_scale(2 ** v2[0]), log_scale(2 ** v2[1])), 
                (log_scale(2 ** v3[0]), log_scale(2 ** v3[1]))]

    green_lines = [
        mp.mpf(input("Enter the exponents of the x-coordinate of the first green line (e.g., for 2^400000 enter 400000): ")),
        mp.mpf(input("Enter the exponents of the x-coordinate of the second green line (e.g., for 2^400000 enter 400000): ")),
    ]
    
    purple_lines = [
        mp.mpf(input("Enter the exponents of the x-coordinate of the first purple line (e.g., for 2^400000 enter 400000): ")),
        mp.mpf(input("Enter the exponents of the x-coordinate of the second purple line (e.g., for 2^400000 enter 400000): "))
    ]
    
    # start_point = (
    #     Decimal(input("Enter the exponents of the x-coordinate of the start point (e.g., for 2^400000 enter 400000): ")),
    # )

    file_path = 'start-coordinate.txt'
    exponent = calculate_exponent(file_path)
    print("Read start-coordinate.txt success, the x-coordinate of start point: 2^", exponent)
    fig, ax = plt.subplots()

    # Draw the triangle
    draw_triangle(vertices, ax)

    # Draw vertical lines
    y_min, y_max = log_scale(2 ** 0), max(vertices, key=lambda v: v[1])[1]
    draw_vertical_lines(purple_lines, y_min, y_max, 'purple', ax)
    draw_vertical_lines(green_lines, y_min, y_max, 'green', ax)
    

    start_point_x = exponent
    y=0

    # Define under limit and over limit
    c1=max(green_lines[0], green_lines[1])
    c2=min(green_lines[0], green_lines[1])

    print("C1, C2", c1, c2)

    if(c2 > start_point_x):
        print("c1 < start_point_x")
        traverse_top(start_point_x,c1,c2,y,ax)
    elif(c1 < start_point_x):
        print("c1 < start_point_x")
        traverse_down(start_point_x,c1,c2,y,ax)

    # plt.show()


if __name__ == "__main__":
    main()
