"""
Define a function isPalindrome() that recognizes palindromes (i.e. words that look the same
written backwards). For example, isPalindrome("radar") should return True .
"""


def is_palindrome(str):
    """palindrome check"""
    if str == str[::-1]:
        return True
    else:
        return False


def main():
    """main function"""
    some_string = 'radar'
    if is_palindrome(some_string):
        print('is palindrome')
    else:
        print('is not palindrome')


if __name__ == "__main__":
    main()

