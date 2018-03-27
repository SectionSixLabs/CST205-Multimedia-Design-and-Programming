#HangmMan Game
#We wiull need random function to get the words out
import random

#WarmUp
#PartA:
def PartA():
  name = requestString("What is your name?")
  print(name)

def PartB():
  word = ""
  while(word != "stop"):
    word = requestString("Enter a word")


#Array of initial words to play
WORDS = "pirate dead".split(',')
LETTERS = "qwertyuiopasdfghjklzxcvbnm"
#Function to draw hangman based on the numb er of guesses
def drawHangMan(n):
  if n==0:
    printNow ("+---+")
    printNow ("|     | ")
    printNow ("|       ")
    printNow ("|       ")
    printNow ("|       ")
    printNow ("|          ")
    printNow ("|=========") 
  elif n==1:
    printNow ("+---+")
    printNow ("|      |   ")
    printNow ("|      o   ")
    printNow ("|          ")
    printNow ("|          ")
    printNow ("|          ")
    printNow ("|=========") 
  elif n==2:
    printNow ("+---+")
    printNow ("|      |   ")
    printNow ("|      o   ")
    printNow ("|      |  ")
    printNow ("|          ")
    printNow ("|          ")
    printNow ("|=========") 
  elif n==3:
    printNow ("+---+")
    printNow ("|      |   ")
    printNow ("|      o   ")
    printNow ("|     /|   ")
    printNow ("|          ")
    printNow ("|          ")
    printNow ("|=========") 
  elif n==4:
    printNow ("+---+")
    printNow ("|      |   ")
    printNow ("|      o   ")
    printNow ("|     /|\  ")
    printNow ("|          ")
    printNow ("|          ")
    printNow ("|=========") 
  elif n==5:
    printNow ("+---+")
    printNow ("|      |   ")
    printNow ("|      o   ")
    printNow ("|     /|\  ")
    printNow ("|     /    ")
    printNow ("|          ")
    printNow ("|=========") 
  elif n==6:
    printNow ("+---+")
    printNow ("|      |   ")
    printNow ("|      o   ")
    printNow ("|     /|\  ")
    printNow ("|     / \  ")
    printNow ("|    RIP   ")
    printNow ("|=========") 
    printNow ("YOU LOST")

def maskWord(word,mask,letter):
  if len(mask)==0:
   firstRun = True 
  else: 
   firstRun = False
  if firstRun: 
   mask=[]
   for char in word: 
    if char==' ' :
      mask.append(" ")
    else:
      mask.append("-")
  else:
   for index in range(0,len(mask)): 
    if word[index]==letter :
       mask[index]=letter
  return mask
  
def gameWin(mask):
    mask= ''.join(mask)
    if int(mask.find('-'))<0:
        return True
    else:
        return False
  
#Clear Screen
def cls(): 
  printNow('\n' *100)
  #prints 100 newlines


def Hangman():
  wordIndex = random.randint(0,len(WORDS)-1)
  word = WORDS[wordIndex]
  guesses = []
  maskStr = maskWord(word,"",'')
  isWin = gameWin(maskStr) 
  while len(guesses)<6 and not isWin:
    cls()
    drawHangMan(len(guesses))
    printNow ("\nYou have used "+str(len(guesses))+" of six guesses")
    printNow ("\nWord so far: "+ ''.join(maskStr))
    drawHangMan(guesses)
    inputLetter = requestString("Guess a letter:").lower()
    if not inputLetter.isalpha() or len(inputLetter)>1:
      printNow ("\nPleas input only a character")
    elif ''.join(maskStr).find(inputLetter)>0:
      printNow("\nYou have already tried this guess")
    elif word.find(inputLetter)<0:
     guesses.append(inputLetter)
     printNow("Incorrect guesses:"+''.join(guesses))
    else:
     maskStr =maskWord(word,maskStr,inputLetter)
     printNow(maskStr) 
     isWin = gameWin(maskStr)
    
  if isWin:
    printNow("\nCongratulations, you win!")
  else:
    cls()
    printNow ("\nYou have used "+str(len(guesses))+" of six guesses")
    drawHangMan(len(guesses))