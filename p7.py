"""
define a function diagonalReverse() that takes matrix (two dimensional array (list) ) and returns
diagonal-reversed one
"""

def diagonal_reverse(arr):
    """diagonal reverse"""
    i = 0
    j = 3
    while i < j:
        arr[i][i], arr[j - 1][j - 1] = arr[j - 1][j - 1], arr[i][i]
#            arr[i][j - 1], arr[j - 1][i] = arr[j - 1][i], arr[i][j - 1]
        i += 1
        j -= 1
# Print matrix after reversals.
    for i in range(3):
        for j in range(3):
            print(arr[i][j], end="  ")
        print()


def main():
    """main function"""
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    diagonal_reverse(matrix)


if __name__ == "__main__":
    main()
