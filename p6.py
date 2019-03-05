"""
Define a function caesarCipher that takes string and key(number) , whuch returns encrypted
string using the Ceasar Cipher
"""


def caesarCipher(text, key):
    """caesar cipher"""
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result


def main():
    """main function"""
    plaintext = input("enter string: ")
    key = int(input("enter key: "))
    print(caesarCipher(plaintext, key))


if __name__ == "__main__":
    main()
