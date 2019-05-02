#Augmented Matrix Solver
import random as r

def run(matrix):
    #check_for_zeroes(matrix)
    for column in range(len(matrix)-1):
        row_reduce(matrix,column)
    return(solve(matrix))

def row_reduce(matrix,column):
    for row in matrix[:column:-1]:
        subtract(matrix[0],row,column)
    

def rand(size,interval):
    #creates a random n x(n+1) matrix 
    matrix = []
    for row in range(size):
        new_row = []
        for column in range(size+1):
            new_row.append(r.randint(interval[0],interval[1]))
        matrix.append(new_row)
    return matrix

def subtract(row1,row2,index):
    multiplier = row2[index]/row1[index]
    for x in range(len(row2)-index):
        row2[x+index] = row2[x+index] - row1[x+index]*multiplier

def check_for_zeroes(matrix):
    for row in matrix:
        if row[0] == 0:
            matrix.append(row)
            matrix.remove(row)

def solve(matrix):
    
    solution = []
    """
    for x in range(len(matrix)):
        rhs = 0
        for y in range(len(matrix)-x-1):
            rhs += matrix[-1-y]
    """
    for row in matrix[::-1]:
        rhs = 0
        pivot = find_pivot(row)
        for entry in row[:row.index(pivot):-1]:
            rhs += entry
        solution.append(rhs/pivot)
    solution.reverse()
    return solution

def find_pivot(row):
    for entry in row:
        pivot = entry
        if pivot != 0:
            return pivot


test = rand(4,[1,10])
