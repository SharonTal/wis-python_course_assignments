import math
import argparse

def circle_calculate(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    print(f"Area of the circle: {area}")
    print(f"Circumference of the circle: {circumference}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate area and circumference of a circle given its radius.")
    parser.add_argument("radius", type=float, help="Radius of the circle")
    args = parser.parse_args()

    circle_calculate(args.radius)
