#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column, num in enumerate(row):
            print("{:d}".format(num), end="")
            if (column < len(row) - 1):
                print(" ", end="")
        print()
