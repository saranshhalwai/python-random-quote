import random 
def prime():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(random.choice(quotes))

if __name__== "__main__":
  prime()
