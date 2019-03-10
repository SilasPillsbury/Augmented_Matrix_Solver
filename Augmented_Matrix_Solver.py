#Augmented Matrix Solver
import random as r

def run(matrix):
    check_for_zeroes(matrix)
    row_reduce(matrix)

def row_reduce(matrix):
    #for row in matrix[:0:-1]:
    pass
    

def rand(size,interval):
    #creates a random n x(n+1) matrix 
    matrix = []
    for row in range(size):
        new_row = []
        for column in range(size+1):
            new_row.append(r.randint(interval[0],interval[1]))
        matrix.append(new_row)
        
    return matrix

def check_for_zeroes(matrix):
    for row in matrix:
        if row[0] == 0:
            matrix.append(row)
            matrix.remove(row)
