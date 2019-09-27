#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: September 2019
# This is a program which can find the volume of an icosahedron.


import math


def main():
#This is what finds the volume of the icosahedron

# Input
    length = int(input("input the edge length of the icosahedron:"))

# Process
    volume = 5*(3+math.sqrt(5))/12*length**3

# Output
    print("")
    print("Then the volume of the icosahedron is {}cm^3" .format(volume))


if __name__ == "__main__":
    main()
