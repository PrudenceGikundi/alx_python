def square_matrix_simple(matrix=[]):
    result = [] 
    for row in matrix:
        square_row = []  
        for element in row:
            square_row.append(element ** 2)  
        result.append(square_row) 
    return result  

if __name__== "__main__":
  matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)