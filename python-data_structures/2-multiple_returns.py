def multiple_returns(sentence):
    sentence_length = len(sentence)
    first_letter = sentence[0] if sentence_length > 0 else None
    return sentence_length, first_letter
if __name__ == "__main__":
   sentence= "0-square_matrix_simple.py"
   length, first = multiple_returns(sentence)
   print("Length: {:d} - First character: {}".format(length, first))