### Michael DeCero
### HomeWork 0501
### 10/16/19
### I have not given or received any unauthorized assistance on this assignment.
### YouTube: https://youtu.be/Mdxj1hwTtb4

import numpy as np

class SixSidedDie:
    'Class that represents a die with six sides (numbers 1 - 6)'
    import random

    def __init__ (self, FaceValue = 6):
        'Initializes a default number for the die (6)'
        self.FaceValue = FaceValue

    def roll (self):
        'Function that returns a random number from 1 - 6 (rolls the die)'
        self.FaceValue = self.random.randrange(1,7)
        return self.FaceValue

    def getFaceValue (self):
        'Function that returns the "face value" of the die that was recently rolled'
        return self.FaceValue

    def __repr__ (self):
        'String representation of SixSidedDie(DieNumber)'
        return 'SixSidedDie({})'.format(self.FaceValue)

class TenSidedDie (SixSidedDie):
    'Class that represents a die with six sides (numbers 1 - 10)'

    def roll (self):
        'Function that returns a random number from 1 - 10 (rolls the die)'
        self.FaceValue = self.random.randrange(1,11)
        return self.FaceValue

    def __repr__ (self):
        'String representation of SixSidedDie(DieNumber)'
        return 'TenSidedDie({})'.format(self.FaceValue)

class TwentySidedDie (TenSidedDie):
    'Class that represents a die with six sides (numbers 1 - 20)'

    def roll (self):
        'Function that returns a random number from 1 - 20 (rolls the die)'
        self.FaceValue = self.random.randrange(1,21)
        return self.FaceValue

    def __repr__ (self):
        'String representation of SixSidedDie(DieNumber)'
        return 'TwentySidedDie({})'.format(self.FaceValue)

class Cup:
    'Class that holds any number of 6 sided dice, 10 sided dice, and 20 sided dice'
    import random

    def __init__ (self, six = 1, ten = 1, twenty = 1):
        'Initializes the default quantity of six, ten, and twenty sided die to be 1 each'
        self.six = six
        self.ten = ten
        self.twenty = twenty

    def roll (self):
        'Function that rolls dice in cup (random number between 1 - 6, random number between 1 - 10, random number between 1 - 20)'
        six = SixSidedDie()                 #Set six, ten, twenty variables to the SixSidedDie, TenSidedDie, and TwentySidedDie Classes, respectively
        ten = TenSidedDie()
        twenty = TwentySidedDie()
        accsix = 0                          #Set accumulators for calculating the sum of dice rolled
        accten = 0
        acctwenty = 0
        strsix = ''                         #Set Accumulator strings for being able to print all dice roll results later
        strten = ''
        strtwenty = ''
        for i in range (int(self.six)):     #For loop run for each of the amount of dice that the user input (six sided, ten sided, and twenty sided)
            six.roll()                      #Roll each die/dice
            accsix += six.getFaceValue()    #Accumulate the sum of the face value of the dice rolled
            strsix += str(six)              #Accumulate the results to show the user later
        for i in range (int(self.ten)):     #See for loop comments above
            ten.roll()
            accten += ten.getFaceValue()
            strten += str(ten)
        for i in range (int(self.twenty)):  #See for loop comments above
            twenty.roll()
            acctwenty += twenty.getFaceValue()
            strtwenty += str(twenty)
        self.six = strsix                   #Set self.six, self.ten, and self.twenty to the completed strings to show the user later
        self.ten = strten
        self.twenty = strtwenty
        self.Total = accsix + accten + acctwenty
        return self.Total                   #Return the total sum of the face value of dice rolled

    def getSum (self):
        'Function that returns the "face value" of the sum of all the dice rolled in the cup'
        return self.Total

    def __repr__ (self):
        'String representation of Cup(Face values of 6 sided dice, Face values of 10 sided dice, and Face Values of 20 sided die)'
        return 'Cup({},{},{})'.format(self.six, self.ten, self.twenty)
