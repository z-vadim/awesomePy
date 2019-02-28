import time


def histogram(arr):
    for elements in arr:
        i = 0
        while i < elements:
            print('*', end='')
            time.sleep(1)
            i += 1
        print()


def main():
    mainarray = [1,2,3,4,5]
    histogram(mainarray)


if __name__ == "__main__":
    main()
