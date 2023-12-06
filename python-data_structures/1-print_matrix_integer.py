def print_matrix_integer(matrix=[[]]):
  matrix = ""
 
  for row in matrix:
    formatted_row = ["{:d}".format(num) for num in row]
    print(*formatted_row)

print_matrix_integer()
  