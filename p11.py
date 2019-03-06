"""
Write a function decToBin() that taces decimal integer and outputs its binary representation.
"""


def decToBin(arg):
    return int(bin(arg)[2:])


def main():
    """main function"""
    print('Enter dec:')
    input_string = input()

    print(decToBin(int(input_string)))


if __name__ == "__main__":
    main()
