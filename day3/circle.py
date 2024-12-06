import math

def circle_calculate():
    radius=int(input("enter radius"))
    area=math.pi * radius**2
    circumference = 2 * math.pi * radius
    print(f"Area of the circle: {area}")
    print(f"Circumference of the circle: {circumference}")



circle_calculate()