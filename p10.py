"""
Write a function charFreq() that takes a string and builds a frequency listing of the characters
contained in it. Represent the frequency listing as Map(Dictionary). Try it with something like
charFreq("abbabcbdbabdbdbabababcbcbab").
"""


def charFreq(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


def main():
    """main function"""
    print('Enter string:')
    input_string = input()

    print(charFreq(input_string))


if __name__ == "__main__":
    main()
