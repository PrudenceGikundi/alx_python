from add_0 import add
from add_0 import fakeAdd
def main():
    a = 1
    b = 2
    sum= add(a, b)
    print ("{}+{}={}".format(a,b,sum))
    diff= fakeAdd(a, b)
    print ("{}+{}={}".format(a,b,diff))

if __name__== "__main__":
  main()
  