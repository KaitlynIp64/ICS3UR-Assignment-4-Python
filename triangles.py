#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program identifies triangles


def main():
    # this function uses a compound boolean statement

    # input
    side1 = input("Please enter side 1: ")
    side2 = input("Please enter side 2: ")
    side3 = input("Please enter side 3: ")
    print("")

    # process & output
    try:
        side1 = int(side1)
    except ValueError:
        print("That is not a valid input.")
    try:
        side2 = int(side2)
    except ValueError:
        print("That is not a valid input.")
    try:
        side3 = int(side3)
    except ValueError:
        print("That is not a valid input.")

    else:
        if side1 == side2 and side1 == side3:
            print("This is an equilateral triangle.")
        elif side1 == side2 or side2 == side3 or side3 == side1:
            print("This is an isosceles triangle.")
        elif side1 != side2 and side2 != side3:
            print("This is a scalene triangle.")


if __name__ == "__main__":
    main()
