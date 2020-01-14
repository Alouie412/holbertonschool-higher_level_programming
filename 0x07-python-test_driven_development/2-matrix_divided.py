#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    matrix_row = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
        return
    if div is 0:
        raise ZeroDivisionError("division by zero")
        return

    matrix_width = len(matrix[0])

    for i in range(0, len(matrix)):
        if len(matrix[i]) != matrix_width:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(0, matrix_width):
            if type(matrix[i][j]) is not int and type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            quotient = '{0:.2f}'.format(matrix[i][j] / div)
            matrix_row.append(quotient)
    new_matrix.append(matrix_row)

    return new_matrix
