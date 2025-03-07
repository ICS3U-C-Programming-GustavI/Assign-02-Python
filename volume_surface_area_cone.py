#!/usr/bin/env python3
# Created by: Gustav Ihlenfeld
# Created on: March 7, 2025
# This program calculates the volume and surface area of a cone

import math


def main():
    # Input: Ask the user for radius, height, and unit
    print(
        "Welcome to the Cone Surface Area and Volume calculator! ☺ Please insert your desired values."
    )

    radius = input("Enter the radius of the cone: ")
    height = input("Enter the height of the cone: ")

    # Error checking (ensures input is a number)
    if not (radius.replace(".", "").isdigit() and height.replace(".", "").isdigit()):
        print("\nError: Please enter valid positive numbers for radius and height.")
        return

    radius = float(radius)
    height = float(height)

    if radius <= 0 or height <= 0:
        print("\nError: Radius and height must be greater than zero.")
        return

    unit = input("Enter the unit of measurement (e.g., cm, m, inches): ")

    # Process: Calculate the volume and surface area
    volume = (1 / 3) * math.pi * (radius**2) * height
    surface_area = math.pi * radius * (radius + height)

    # Output: Show rounded results with units
    print("\n--- Cone Measurements ---")
    print("Volume: {:.2f} {}³".format(volume, unit))
    print("Surface Area: {:.2f} {}²".format(surface_area, unit))


if __name__ == "__main__":
    main()
