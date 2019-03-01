"""
Define a function, which takes a string with N opening brackets
("[") and N closing brackets ("]") , in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it consists entirely of pairs
of opening/closing brackets (in that order), none of which mis-nest.
"""


def check_brackets(string):
    """work with brackets"""

    opened_brackets = ('(', '[', '{', '<')
    closed_brackets = (')', ']', '}', '>')
    temp_buffer = []
    for i in string:
        if i in opened_brackets:
            temp_buffer.append(i)
        elif i in closed_brackets:
            pos = closed_brackets.index(i)
            if ((len(temp_buffer) > 0) and (opened_brackets[pos] == temp_buffer[len(temp_buffer) - 1])):
                temp_buffer.pop()
            else:
                return 'NOT OK'
    if len(temp_buffer) == 0:
        return 'OK'


def main():
    """main function"""

    print('Enter string with N opening brackets ("[") and N closing brackets ("]"):')
    input_string = input()
    print(input_string + ' ' + check_brackets(input_string))


if __name__ == "__main__":
    main()
