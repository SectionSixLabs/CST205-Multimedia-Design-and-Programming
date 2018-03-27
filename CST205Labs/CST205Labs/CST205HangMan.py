#HangmMan Game
#Sergiy Zarubin
#Danny Tran
#We will need random function to get the words out
import random

#WarmUp
#PartA:
def PartA():
  name = requestString("What is your name?")
  printNow(name)

def PartB():
  word = ""
  while(word != "stop"):
    word = requestString("Enter a word")


#Array of initial words to play
WORDS = "pirate dead,asinine,colloquial,commiserate,diatribe,discern,formidable,gregarious,incessant,invariably,meager,plausible,quintessential,sardonic,stoic tedious".split(',')
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
  cls()
  #Output a brief description of hangman and how to play
  printNow("You have 6 guess to find correct word.")
  wordIndex = random.randint(0,len(WORDS)-1)
  word = WORDS[wordIndex]
  guesses = []
  maskStr = maskWord(word,"",'')
  isWin = gameWin(maskStr) 
  while len(guesses)<6 and not isWin:
    #cls()
    drawHangMan(len(guesses))
    if len(guesses)>0:
      printNow("Incorrect guesses:"+''.join(guesses))
    printNow ("\nYou have used "+str(len(guesses))+" of six guesses")
    printNow ("\nWord so far: "+ ''.join(maskStr))
    drawHangMan(guesses)
    inputLetter = requestString("Guess a letter:").lower()
    if not inputLetter.isalpha() or len(inputLetter)>1:
      printNow ("\nPleas input only a character")
    elif ''.join(maskStr).find(inputLetter)>0 or ''.join(guesses).find(inputLetter)>0 :
      printNow("\nYou have already tried this guess")
    elif word.find(inputLetter)<0:
      if ''.join(guesses).find(inputLetter)<0:
         guesses.append(inputLetter)
      else:
         printNow("\nYou have already tried this guess")
    else:
     maskStr =maskWord(word,maskStr,inputLetter)
     isWin = gameWin(maskStr)
    
  if isWin:
    printNow(word.upper())
    printNow("\nCongratulations, you win!")
  else:
    cls()
    printNow ("\nYou have used "+str(len(guesses))+" of six guesses")
    drawHangMan(len(guesses))