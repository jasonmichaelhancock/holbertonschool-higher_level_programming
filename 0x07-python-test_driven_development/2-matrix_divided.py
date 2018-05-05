#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = [row[:] for row in matrix]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] = round((new_matrix[i][j] / div), 2)
    return(new_matrix)
