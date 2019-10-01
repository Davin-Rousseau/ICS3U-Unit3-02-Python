#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on September 2019
# This program asks user to pick a number from 0-9
# and tells them if they got it right or wrong


import constants


def main():
    # This function makes the user guess a number from 0-9

    # input
    number1 = int(input("Guess my number (0-9): "))
    print("")

    # process
    if number1 == constants.MAIN_NUMBER:
        #output
        print("Correct!")

    if number1 != constants.MAIN_NUMBER:
        #output
        print("Wrong!")


if __name__ == "__main__":
    main()
