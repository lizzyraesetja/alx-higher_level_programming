#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        field = []
        for j in range(len(matrix[i])):
            field.append(matrix[i][j] ** 2)
        new_matrix.append(field)
    return(new_matrix)
