"""
Write a function game() number-guessing game, that takes 2 int parameters defining the range.
Use some kind of random function to generate random int from the range. While user input isn’t
equal that number, print “Try again!”. If user guess the number, congratulate him and exit.
"""
import random


def game(start, end):
    """randomize from range"""
    winner_digit = random.randint(start, end)
    while int(input("enter some digit: \n")) != winner_digit:
        print("Try again!")
    else:
        print('You win! Bye!')



def main():
    """main function"""
    game(0, 5)


if __name__ == "__main__":
    main()
