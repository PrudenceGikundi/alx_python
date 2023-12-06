def print_matrix_integer(matrix=[[]]):
  matrix = [[1, 2, 3], 
          [4, 5, 6],
          [7, 8, 9]]
 
  for row in matrix:
    formatted_row = ["{:d}".format(num) for num in row]
    print(*formatted_row)
print_matrix_integer()
  