#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for l in range(len(matrix)):
        for k in range(len(matrix[l])):
            print("{:d}".format(matrix[l][k]), end="")
            if k != (len(matrix[l]) - 1):
                print(" ", end="")

        print("")
