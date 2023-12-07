def square_matrix_simple(matrix=[]):
    result_matrix = [] 
    for row in matrix:
        square_row = []  
        for element in row:
            square_row.append(element ** 2)  
        result_matrix.append(square_row) 
    return result_matrix  

if __name__== "__main__":
  matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]

  new_matrix = square_matrix_simple(matrix)
  print(new_matrix)
  print(matrix)