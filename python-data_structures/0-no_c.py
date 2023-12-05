def no_c(my_string):
  #empty variable new_string to store our output
  new_string= "" 
  #iterate through each character
  for char in my_string:
    # Check if the current character is NOT equal to'c' and'C' using the in operator
    if char not in ["c","C"]:
        # If true, it is not c or C, so append (+=) the char to new_string
      new_string += char
  return new_string
# print(no_c("I love Coconut and Corn"))
  