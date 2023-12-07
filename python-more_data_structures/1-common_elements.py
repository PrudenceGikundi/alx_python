def common_elements(set_1, set_2):
    combinedset = set()

    for item in set_1:
        if item in set_2 :
            combinedset.add(item)

    return combinedset


if __name__=="__main__":
  set_1 = { "Python", "C", "Javascript" }
  set_2 = { "Bash", "C", "Ruby", "Perl" }
  c_set = common_elements(set_1, set_2)
  print(sorted(list(c_set)))