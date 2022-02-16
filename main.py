from random import randint
def generateWord():
  wordListTxt = open("wordList.txt", "r")
  # Store words in an array since we want to pull one at a random index
  wordList = [i[:-1] for i in wordListTxt if (len(str(i)) == 6)] # Char count is 6 including "\n"
  wordListTxt.close()
  return wordList[randint(0, len(wordList)-1)]

def check(guess, answer):
  arr = ["⬛"] * 5
  counter = 0
  x = [i for i in answer]
  for c, i in enumerate(guess):
    if i.lower() == answer[c].lower():
      arr[c] = "🟩"
      x.pop(c - counter)
      counter += 1
  for c, i in enumerate(guess):
    if i in x and arr[c] != "🟩":
      arr[c] = "🟨"
  
  return arr

def main():
  a = generateWord()
  g = ""
  tracker = []
  for k in range(6):
    g = input("\nGuess a word: ")
    while(len(g) != 5):
      g = input("Incorrect word length!\nGuess a word:")
    t = check(g, a)
    tracker.append(t)
    if(g.lower() == a.lower()):
      break
    for i in t:
      print(i, end=" ")
  print("\n\nSummary: ")
  for i in tracker:
    for j in i:
      print(j, end = " ")
    print("\n")
  
if __name__ == "__main__":
  main()

