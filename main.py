from random import randint

def generateWord():
  wordListTxt = open("wordList.txt", "r")
  # Store words in an array since we want to pull one at a random index
  wordList = [i[:-1] for i in wordListTxt if (len(str(i)) == 6)] # Char count is 6 including "\n"
  wordListTxt.close()
  return wordList[randint(0, len(wordList)-1)]

def main():
  ans = generateWord()
  



if __name__ == "__main__":
  main()

