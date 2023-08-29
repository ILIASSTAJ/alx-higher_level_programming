#!/usr/bin/python3
''' function that prints a matrix of integers'''


def print_matrix_integer(matrix=[[]]):
    for test in matrix:
        print("{}".format(test))
        for col in test:
            print("{}".format(col),end = " " if col !=  test[-1] else  " end")
        print()

