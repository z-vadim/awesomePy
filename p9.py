def check_brackets(string):
    opened_brackets = ('(', '[', '{', '<')
    closed_brackets = (')', ']', '}', '>')
    temp_buffer = []
    for i in string:
        if i in opened_brackets:
            temp_buffer.append(i)
        if i in closed_brackets:
            if len(temp_buffer) == 0:
                return 'NOT OK'
            if temp_buffer[-1] == opened_brackets:
                temp_buffer = temp_buffer[:-1]
            else:
                return 'NOT OK'
    return 'OK'


def main():
    print('Enter string with N opening brackets ("[") and N closing brackets ("]"):')
    input_string = input()
    print(input_string + ' ' + check_brackets(input_string))


if __name__ == "__main__":
    main()
