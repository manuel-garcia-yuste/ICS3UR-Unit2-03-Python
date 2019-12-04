#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : December 2019
# This program calculates circumference in cm


import constants


def main():
    # input
    circumference = float(input("What is the radius: "))

    # process
    circumference = constants.TAU * circumference

    # output
    print("The circumference is " + str(round(circumference, 2)) + " cm.")


if __name__ == "__main__":
    main()
