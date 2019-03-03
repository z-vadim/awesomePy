"""
Define a function reverse() that computes the reversal of a string. For example,
reverse("I am testing") should return the string “gnitset ma I”.
"""


def reverse(str):
    """reverse function"""
    result = ""
    for i in str[::-1]:
        result += i
    return result


def main():
    """main function"""
    some_string = 'I am testing'
    print(reverse(some_string))


if __name__ == "__main__":
    main()

