word= "Holberton"
word_first_3= "Hol"
word_last_2="on"
middle_word="olberto"
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
newword_first_3 = word_first_3.replace("Hol", "sch")
newword_last_2 = word_last_2.replace("on", "ol")
newmiddle_word = middle_word.replace("olberto", "choo")
print(newword_first_3)
print(newword_last_2)
print(newmiddle_word)
