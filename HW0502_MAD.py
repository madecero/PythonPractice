### Michael DeCero
### HomeWork 0502
### 10/17/19
### I have not given or received any unauthorized assistance on this assignment.
### YouTube: https://youtu.be/I82PcJ7ByJM

from diceSettings import *
import random

def HW0502():
    'Function that facilitates the game of Cups & Dice'
    Name = GreetUser()                              #Greets User and gets his or her name
    UserBalance = 100                               #Estabilishes a "bank" balance of $100
    UserAnswer = AskUserGame()                      #Asks user if he or she wants to play a game
    while UserAnswer.upper() == 'Y':                #Will continue to play the game if user inputs 'Y'
        print ('\n')
        print ('Your Balance is $' + str(UserBalance))  #Tells the user how much they have to bet
        Bet = GetUserBet()                          #Obtains and saves the amount the user wants to bet
        Goal = GenerateGoal()                       #Obtains and saves what the goal number is that the user is striving (rolling) for
        DiceTotal, Roll = DisplayRoll()             #Rolls the amount of dice the user input
        BetResult = CalcWinLoss(Bet, Goal, DiceTotal) #Obtains and saves the bet result depending on the roll + the result of the cup roll
        UserBalance += BetResult
        PrtAnswer(Name, UserBalance, BetResult, Goal, DiceTotal, Roll) #Tells the user if he/she won, the results of the roll, and how much he/she won/lost
        UserAnswer = AskUserGame()                  #If user wants to continue, loop to play another game
    print ('\n' + 'You do not want to play any more? Bummer. See ya later.')

def GreetUser():
    "Function that greets the user and takes in the input of the user's first name"
    Name = input("Hello. Welcome to the Cups & Dice Game! Please enter your first name in quotes (''): ")
    print ('\n')
    return Name

def AskUserGame():
    'Function that asks the user if he or she wants to play a game of Cups & Dice'
    UserAnswer = eval(input("Are you ready to play another game of Cups & Dice? ('Y' or 'N') "))
    return UserAnswer

def GetUserBet():
    'Function that asks the user how much of their balance they want to wager'
    Bet = eval(input('How much of your balance would you like to wager? '))
    while Bet <= 0:                                 #Raise Error if a negative number is entered
        print ('\n')
        print (ValueError('You must enter a positive integer for your bet.'))
        print ('\n')
        Bet = eval(input('How much of your balance would you like to wager? '))
    return Bet

def GenerateGoal():
    'Function that generates a random number between 1 and 100 - this number will be the goal the user is striving for'
    Goal = random.randrange(1,100)
    print ('\n')
    print ('The number you are rolling for is ' + str(Goal))
    print ('\n')
    return Goal

def GetDiceQuantity():
    'Function that asks the user how many of each type of dice they want to roll in the cup'
    SixDice, TenDice, TwentyDice = map(int,input('What is the quantity of each type of die that you would like to roll? (Quantity of 6 sided die, Quantity of 10 sided die, Quantity of 20 sided die) ').split(','))
    return SixDice, TenDice, TwentyDice

def DisplayRoll():
    'Function that rolls cup of dice'
    SixDice, TenDice, TwentyDice = GetDiceQuantity() #Pulls user input of quantities of dice from the GetDiceQuantity function above
    cup = Cup(SixDice, TenDice, TwentyDice)     #Sets the quantities of six sided dice, ten sided dice, and twenty sided dice provided as input by user from the GetDiceQuantity function
    cup.roll()                                  #Rolls dice
    DiceTotal = cup.getSum()                    #Sums the face values of the dice
    Roll = cup                                  #Captures the face values of each die rolled
    return DiceTotal, Roll

def CalcWinLoss(Bet, Goal, DiceTotal):
    "Function that calculates the user's total win or loss as well as updated balance depending on the bet and the results of the dice roll"
    if DiceTotal == Goal:                       #Sum of dice = goal
        Bet *= 10                               #User wins 10 times his or her bet
    elif (Goal - 3) <= DiceTotal < Goal:        #Sum of dice is within 3 or less of goal
        Bet *= 5                                #User wins 5 times his or her bet
    elif (Goal - 10) <= DiceTotal < Goal:       #Sum of dice is within 10 or less of goal
        Bet *= 2                                #User wins twice his or her bet
    else:
        Bet = 0 - Bet                           #User loses bet
    return Bet                                  #Return the result of the wager +/- the result of the roll

def PrtAnswer(Name, UserBalance, BetResult, Goal, DiceTotal, Roll):
    'Function that tells the user if he/she won, the results of the roll, and how much he/she won/lost'
    if BetResult < 0:                           #If BetResult < 0, user lost - print the total face value result and the face value of each die
        print ('\n')
        print ('Sorry ' + Name + '. You lost your bet.')
        print ('Your updated balance is $' + str(UserBalance) + '\n')
    else:                                       #If BetResult > 0, user won! - print the total face value result and the face value of each die
        print ('\n')
        print ('Congratulations ' + str(Name) + '! You won $' + str(BetResult))
        print ('Your updated balance is $' + str(UserBalance) + '\n')
    print ('Below are the results of your roll:' + '\n')
    print (str(Roll) + '\n') 
    print ('Goal = ' + str(Goal)) 
    print ('Total = ' + str(DiceTotal))
    print ('\n')
    
HW0502()
