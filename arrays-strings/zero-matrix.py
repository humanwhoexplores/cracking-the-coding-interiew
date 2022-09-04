"""
    in a M*N matrix L if any element is 0 
    then its entire row and column is set to 0
"""

def zeroMatrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    row_bool = [False] * num_rows
    col_bool = [False] * num_cols

    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 0:
                row_bool[i] = True
                col_bool[j] = True 
    
    for i in range(num_rows):
        if row_bool[i] == True:
            # Marking all the elements as 0
            for j in range(num_cols):
                matrix[i][j] = 0
    
    for j in range(num_cols):
        if col_bool[i] == True:
            # Mark all elements as 0
            for i in range(num_rows):
                matrix[i][j] = 0

def printMatrix(matrix):

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_rows):
        for j in range(num_cols):
            print(matrix[i][j])

if __name__ == '__main__':
    matrix = [[1, 0, 3], [0, 5, 6], [0, 8, 9]]
    zeroMatrix(matrix)
    printMatrix(matrix)
