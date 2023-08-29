#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    function that computes the square value of
    all integers of a matrix
    '''

    new_list = []
    if len(matrix) == 0:
        return new_list
    for row in matrix:
        a = []
        for col in row:
            a.append(col ** 2)
        new_list.append(a)
    return new_list

    #new_list = [[i*i for i in j] for j in matrix]
    #return new_list
