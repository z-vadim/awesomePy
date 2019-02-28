def sum(arr):
    elements = 0
    for elements in arr:
        print('+%s' %elements)
        elements += elements
        # i = 0
        # while i < len(arr):
        #     elements += elements
        #     i += 1
    print(elements)


#def multiply(arr):

def main():
    mainarray = [1, 2, 3, 4, 5]
    sum(mainarray)


if __name__ == "__main__":
    main()