#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix == [[]]):
        print()
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j + 1 == len(matrix[i]):
                    last = ' '
                else:
                    last = ' '
                print('{:d}'.format(matrix[i][j], end = last))
