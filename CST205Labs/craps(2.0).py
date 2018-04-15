# Partner: Sergiy Zarubin
# Lab 15
# Python Version 3
# April 11th 2018

import random
import time 

# Problem 1: Write a function to build a program that let's users play craps
# Craps rules: 1) player rolls 2 6-sided dice and adds the numbers together
# 2) First roll, 7 or 11 win(game ends), 2 or 3 or 12 lose(game ends)
# 2) 4, 5, 6, 8, 9, 10 rolled, number becomes "point"
# 3) player rolls a 2nd time: a 7 == lose or point == win
affirmation = ['yes', 'y', 'yea', 'yeah', 'yaeh', 'yee']
lacks_affirm = ['n', 'no', 'nah', 'nope', 'meh']
# single dice function:
def roll_the_dice():
    printNow("The dice are rolling...")
    time.sleep(2)
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    total = dice_1+dice_2
    printNow("Dice One: %d" % dice_1)
    printNow("Dice two: %d" % dice_2)
    printNow("You rolled a %d" % total)
    printNow("\n")
    return int(total)

# ready to play function
def ready_to_play():
    global affirmation
    global lacks_affirm
    ready_now = requestString("Ready to play? ")
    ready_now.islower()
    if ready_now in affirmation:
        printNow("\nRoll those dice!\n")
    elif ready_now in lacks_affirm:
        printNow("I will wait.")
        sleep(3)
        printNow("Okay let's Play!\n")
    else:
        printNow("Sorry, I didn't get that. Let's just play.\n")

# printNow review funtion
def display_review():
    printNow('''To play: \nRoll the dice. \n1st roll: if dice combined is 7 or 11, Player Wins! If dice combined is 2, 3, 12, Player Loses! Any other numbers
become a point. \n2nd roll: Roll a 7 and instantly lose, roll a point and
Win!\n''')

# game introduction function
def intro():
    global affirmation
    showWarning("You need JES Version 5.01 or later to run this program")
    ready = requestString("""Ready to play Craps(\"yes\") or do you need a review(\"review\")?""")
    review_aff = ['review', 'Review', 'R', 'r']
    if ready in affirmation:
        printNow("Let's play Craps!\n")
    elif ready in review_aff:
        display_review()
        ready_to_play()
    else:
        printNow("\nSorry, I didn't get it. Let's review, then play.\n")
        display_review()
        ready_to_play()

# return the total to check the win
def check_win(total):
    return total


def craps_main():
    global affirmation
    global lacks_affirm
    intro()
    play_again = 'yes'
    while play_again not in lacks_affirm:
        total = roll_the_dice()
        first_total = check_win(total)
        first_total_options = [2, 3, 12]
        if ((first_total == 7) or (first_total == 11)):
            printNow("You Won!")
        elif (first_total in first_total_options):
            printNow("You Lost :(")
        else:
            total_two = roll_the_dice()
            second_total = check_win(total_two)
            if second_total == 7:
                printNow("You Lost :(")
            else:
                printNow("You Won!")
        play_again = requestString("Do you want to play again? ")
        printNow("------------------------------------------------------------")
    printNow("\nThanks for playing!")

craps_main()