### MADmind, LLC.
### Make Up Your Mind_DayCare
### v1 2/28/2020

# Future Considerations:
# - Consider adding additional branching for different "tiers" of kids (e.g., infant is more expensive than toddler)

def MakeUpYourMind():
    'Function that helps the user make up his or her mind!'
    print ('\n')
    print ('00      00     00     0000            1          0')
    print ('0 0    0 0    0  0    0   0  00   00     000     0')
    print ('0  0  0  0   0 00 0   0   0  0 0 0 0  1  0  0  0 0')
    print ('0   0    0  0      0  0000   0  0  0  1  0  0  0 0')
    print ('\n')
    print ('Hello and welcome to MADmind. I am going to help make up your mind!')
    print ('\n')
    print ("It sounds like you need help making a decision about day care. Let's get some information from you.")
    print ('\n')
    print ('If, at any point, you enter a mistake in one of your entries, you may enter 0 for the remainder of the questions until you get asked if you want to go through the program again.')
    print ('Then, you will be able to start over.')
    NumKids = GetKids()                             #Greets user and asks how many kids they will need in daycare for the next month
    DCcost2 = GetDCcost2()                          #Asks user how much day care is for 2 days a week per child
    DCcost3 = GetDCcost3()                          #Asks user how much day care is for 3 days a week per child
    DCcost4 = GetDCcost4()                          #Asks user how much day care is for 4 days a week per child
    DCcost5 = GetDCcost5()                          #Asks user how much day care is for 5 days a week per child
    Wage = GetWage()                                #Gets user's hourly wage
    WkndDays = GetWkndDays()                        #Asks user how many weekend days he or she is willing to work
    Net2, Net3, Net4, Net5 = CalcBEpoint(DCcost2, DCcost3, DCcost4, DCcost5, Wage, WkndDays, NumKids)   #Calculates best mix of working days and days at daycare
    prtAnswer(Net2, Net3, Net4, Net5, DCcost2, DCcost3, DCcost4, DCcost5) #Gives user best option for amount of days in daycare given the current wage and the calculated hourly DCcost
    print ('\n')
    GoAgain = AnotherRound()                        #Loops if user wants to go through the program again - the functions below are all repeats of functions above
    while GoAgain.upper() == 'Y' or GoAgain.upper() == 'YES':
        NumKids = GetKids()
        DCcost2 = GetDCcost2()
        DCcost3 = GetDCcost3()
        DCcost4 = GetDCcost4()
        DCcost5 = GetDCcost5()
        Wage = GetWage()
        WkndDays = GetWkndDays()
        Net2, Net3, Net4, Net5 = CalcBEpoint(DCcost2, DCcost3, DCcost4, DCcost5, Wage, WkndDays, NumKids)
        prtAnswer(Net2, Net3, Net4, Net5, DCcost2, DCcost3, DCcost4, DCcost5)
        print ('\n')
        GoAgain = AnotherRound()
    print ('\n')
    print ('Thank you for visiting MADmind. I hope to see you again soon!')

def GetKids():
    'Function that greets user and asks how many kids they will need in daycare for the next month.'
    print ('\n')
    while True:
        try:
            NumKids = eval(input("How many kids do you have that need to be in daycare? "))
        except:
            print("Please enter a number (and only a number) greater than zero.")
            continue                                                            #better try again... Return to the start of the loop
        else:
            break                                                               #it worked! we're ready to exit the loop.
    while type(NumKids) is not int:
        print("Please enter a number (and only a number) greater than zero.")
        while True:
            try:
                NumKids = eval(input("How many kids do you have that need to be in daycare? "))
            except:
                print("Please enter a number (and only a number) greater than zero.")
                continue                                                        #better try again... Return to the start of the loop
            else:
                break                                                           #it worked! we're ready to exit the loop.
    return NumKids

def GetDCcost2():
    'Function that asks user how much day care is for 2 days a week per child.'
    print ('\n')
    print ('Enter the dollars per month of how much your day care of choice costs per child (no dollar signs and no commas - only a single number) ')
    print ("If there is not an option for the amount of days in question, please enter the number 0.")
    print ('\n')
    while True:
        try:
            DCcost2 = eval(input('Cost for 2 days per week (if 2 days a week is not an option, please enter the number 0): '))
        except:
            print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
            continue                                                            #better try again... Return to the start of the loop
        else:
            break                                                               #it worked! we're ready to exit the loop.
    while type(DCcost2) is not int:
        print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
        while True:
            try:
                DCcost2 = eval(input('Cost for 2 days per week (if 2 days a week is not an option, please enter the number 0): '))
            except:
                print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
                continue                                                        #better try again... Return to the start of the loop
            else:
                break                                                           #it worked! we're ready to exit the loop.
    return DCcost2

def GetDCcost3():
    'Function that asks user how much day care is for 3 days a week per child.'
    print ('\n')
    while True:
        try:
            DCcost3 = eval(input('Cost for 3 days per week (if 3 days a week is not an option, please enter the number 0): '))
        except:
            print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
            continue                                                            #better try again... Return to the start of the loop
        else:
            break                                                               #it worked! we're ready to exit the loop.
    while type(DCcost3) is not int:
        print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
        while True:
            try:
                DCcost3 = eval(input('Cost for 3 days per week (if 3 days a week is not an option, please enter the number 0): '))
            except:
                print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
                continue                                                        #better try again... Return to the start of the loop
            else:
                break                                                           #it worked! we're ready to exit the loop.
    return DCcost3

def GetDCcost4():
    'Function that asks user how much day care is for 4 days a week per child.'
    print ('\n')
    while True:
        try:
            DCcost4 = eval(input('Cost for 4 days per week (if 4 days a week is not an option, please enter the number 0): '))
        except:
            print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
            continue                                                            #better try again... Return to the start of the loop
        else:
            break                                                               #it worked! we're ready to exit the loop.
    while type(DCcost4) is not int:
        print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
        while True:
            try:
                DCcost4 = eval(input('Cost for 4 days per week (if 4 days a week is not an option, please enter the number 0): '))
            except:
                print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
                continue                                                        #better try again... Return to the start of the loop
            else:
                break                                                           #it worked! we're ready to exit the loop.
    return DCcost4

def GetDCcost5():
    'Function that asks user how much day care is for 5 days a week per child.'
    print ('\n')
    while True:
        try:
            DCcost5 = eval(input('Cost for 5 days per week (if 5 days a week is not an option, please enter the number 0): '))
        except:
            print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
            continue                                                            #better try again... Return to the start of the loop
        else:
            break                                                               #it worked! we're ready to exit the loop.
    while type(DCcost5) is not int:
        print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
        while True:
            try:
                DCcost5 = eval(input('Cost for 5 days per week (if 5 days a week is not an option, please enter the number 0): '))
            except:
                print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
                continue                                                        #better try again... Return to the start of the loop
            else:
                break                                                           #it worked! we're ready to exit the loop.
    return DCcost5

def GetWage():
    "Function that gets user's hourly wage."
    print('\n')
    while True:
        try:
            Wage = eval(input("Please enter your hourly wage (no dollar signs and no commas - only a single number): "))
        except:
            print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
            continue                                                            #better try again... Return to the start of the loop
        else:
            break                                                               #it worked! we're ready to exit the loop.
    while type(Wage) is tuple:
        print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
        while True:
            try:
                Wage = eval(input("Please enter your hourly wage (no dollar signs and no commas - only a single number): "))
            except:
                print("Please enter a number, and only a number - no commas, no dollar signs, no text.")
                continue                                                        #better try again... Return to the start of the loop
            else:
                break                                                           #it worked! we're ready to exit the loop.
    return Wage

def GetWkndDays():
    'Asks user how many weekend days he or she is willing to work'
    print ('\n')
    while True:
        try:
            WkndDays = eval(input('How many weekend days a week are you willing/able to work (max days = 2)? '))
        except:
            print("Please only enter a single number (0, 1, or 2). Do NOT include text.")
            continue                                                            #better try again... Return to the start of the loop
        else:
            break                                                               #it worked! we're ready to exit the loop.
    while type(WkndDays) is not int:
        print("Please only enter a single number (0, 1, or 2). Do NOT include text.")
        while True:
            try:
                WkndDays = eval(input('How many weekend days a week are you willing/able to work (max days = 2)? '))
            except:
                print("Please only enter a single number (0, 1, or 2). Do NOT include text.")
                continue                                                        #better try again... Return to the start of the loop
            else:
                break                                                           #it worked! we're ready to exit the loop.
    while not 0 <= WkndDays  <= 2:
        print("Please only enter a single number (0, 1, or 2). Do NOT include text.")
        while True:
            try:
                WkndDays = eval(input('How many weekend days a week are you willing/able to work (max days = 2)? '))
            except:
                print("Please only enter a single number (0, 1, or 2). Do NOT include text.")
                continue                                                        #better try again... Return to the start of the loop
            else:
                break                                                           #it worked! we're ready to exit the loop.
    return WkndDays

def CalcBEpoint(DCcost2, DCcost3, DCcost4, DCcost5, Wage, WkndDays, NumKids):
    'Function that calculates best mix of working days and days at daycare.'
    DailyWage = Wage*8
    MonthAdj = 4+(1/3)                                                          #To calculate average monthly nets below
    if DCcost2 == 0:
        Net2 = 0                                                                #If 2 days a week is not an option, return 0
    else:
        Net2 = int((DailyWage*(2+WkndDays)*MonthAdj) - DCcost2*NumKids)         #Else, calculate the cash flow of Total Wages minus Total DayCare Costs
    if DCcost3 == 0:
        Net3 = 0                                                                #If 3 days a week is not an option, return 0
    else:
        Net3 = int((DailyWage*(3+WkndDays)*MonthAdj) - DCcost3*NumKids)         #Else, calculate the cash flow of Total Wages minus Total DayCare Costs
    if DCcost4 == 0:
        Net4 = 0                                                                #If 4 days a week is not an option, return 0
    else:
        if WkndDays == 2:
            Net4 = int(((DailyWage*5 + DailyWage*1.5)*MonthAdj) - DCcost4*NumKids)  #Calculate the cash flow with time and a half included
        else:
            Net4 = int((DailyWage*(4+WkndDays)*MonthAdj) - DCcost4*NumKids)         #Else, calculate the cash flow of Total Wages minus Total DayCare Costs
    if DCcost5 == 0:
        Net5 = 0                                                                #If 5 days a week is not an option, return 0
    else:
        if WkndDays > 0:
            Net5 = int(((DailyWage*5 + (DailyWage*WkndDays)*1.5)*MonthAdj) - DCcost5*NumKids) #Calculate the cash flow with time and a half included
        else:
            Net5 = int((DailyWage*(5+WkndDays)*MonthAdj) - DCcost5*NumKids)     #Else, calculate the cash flow of Total Wages minus Total DayCare Costs
    return Net2, Net3, Net4, Net5

def AnotherRound():
    'Loops if user wants to go through the program again.'
    while True:
        try:
            GoAgain = eval(input("Would you like to go through the program again with different inputs? (Please enter either 'Y' or 'N' in quotes ('')) "))
        except:
            print("Please enter either 'Y' or 'N' in quotes ('').")
            continue                                                            #better try again... Return to the start of the loop
        else:
            break                                                               #it worked! we're ready to exit the loop.
    while type(GoAgain) is not str:
        print("Please enter either 'Y' or 'N' in quotes ('').")
        while True:
            try:
                GoAgain = eval(input("Would you like to go through the program again with different inputs? (Please enter either 'Y' or 'N' in quotes ('')) "))
            except:
                print("Please enter either 'Y' or 'N' in quotes ('').")
                continue                                                        #better try again... Return to the start of the loop
            else:
                break                                                           #it worked! we're ready to exit the loop.
    return GoAgain

def prtAnswer(Net2, Net3, Net4, Net5, DCcost2, DCcost3, DCcost4, DCcost5):
    'Function that gives user best option for amount of days in daycare given the current wage and the calculated hourly DCcost'
    NegativeList = []                                                           #Set empty list that will be used later
    NetList = [Net2, Net3, Net4, Net5]                                          #List of all cashflow outputs
    for i in NetList:
        if i < 0:
            NegativeList.append(i)                                              #identifies negative values so that the user can be notified of detrimental options in the print statements below
    BestOption = max(NetList)                                                   #identify the highest number that is calculated from the CalcBEpoint function above
    if BestOption == NetList[0]:
        OptionDays = '2 days per week'                                          #2 days per week generates the highest number
    elif BestOption == NetList[1]:
        OptionDays = '3 days per week'                                          #3 days per week generates the highest number
    elif BestOption == NetList[2]:
        OptionDays = '4 days per week'                                          #4 days per week generates the highest number
    elif BestOption == NetList[3]:
        OptionDays = '5 days per week'                                          #5 days per week generates the highest number
    print ('\n')                                                                #Print output below
    print ('************************************************************************************************************************************************************')
    print ('Thank you!')
    if len(NegativeList) == 0:                                                  #The user makes enough money to choose.
        print ('It is your choice on how many days you want your child(ren) to attend daycare. Your mix of income and daycare cost afford you flexibilty in your decision making.')
    elif len(NegativeList) == 1:                                                #The user does not make enough money to support only 2 days at daycare. They need to work more than that
        if DCcost3 == 0 and DCcost4 == 0 and DCcost5 == 0:
            print ('Based on your inputs, I suggest either finding a different daycare that gives you more options, or working more weekend days (if possible).')
        elif DCcost2 == 0 and DCcost4 == 0 and DCcost5 == 0:
            print ('Based on your inputs, I suggest either finding a different daycare that gives you more options, or working more weekend days (if possible).')
        elif DCcost2 == 0 and DCcost3 == 0 and DCcost5 == 0:
            print ('Based on your inputs, I suggest either finding a different daycare that gives you more options, or working more weekend days (if possible).')
        elif DCcost2 == 0 and DCcost3 == 0 and DCcost4 == 0:
            print ('Based on your inputs, unless you are willing/able to work more weekend days, this daycare option is unfortunatley not affordable for your current wages.')
        elif DCcost3 == 0 and DCcost4 == 0:
            print ('Based on your inputs, the least amount of days you would want to have your child(ren) attend daycare is 5 days per week.')
            print ('\n')
            print ('Unless you are willing/able to work more weekend days, having your child attend day care less than 5 days per week means that your income will suffer to a point that the cost of daycare would, lead to weekly financial losses.')
        elif DCcost3 == 0:
            print ('Based on your inputs, the least amount of days you would want to have your child(ren) attend daycare is 4 days per week.')
            print ('\n')
            print ('Unless you are willing/able to work more weekend days, having your child attend day care less than 4 days per week means that your income will suffer to a point that the cost of daycare would, lead to weekly financial losses.')
        else:
            print ('Based on your inputs, the least amount of days you would want to have your child(ren) attend daycare is 3 days per week.')
            print ('\n')
            print ('Unless you are willing/able to work more weekend days, having your child attend day care less than 3 days per week means that your income will suffer to a point that the cost of daycare would, lead to weekly financial losses.')
    elif len(NegativeList) == 2:                                                #The user does not make enough money to support only 3 days at daycare. They need to work more than that
        if DCcost4 == 0 and DCcost5 == 0:
            print ('Based on your inputs, I suggest either finding a different daycare that gives you more options, or working more weekend days (if possible).')
        elif DCcost3 == 0 and DCcost5 == 0:
            print ('Based on your inputs, I suggest either finding a different daycare that gives you more options, or working more weekend days (if possible).')
        elif DCcost2 == 0 and DCcost5 == 0:
            print ('Based on your inputs, I suggest either finding a different daycare that gives you more options, or working more weekend days (if possible).')
        elif DCcost2 == 0 and DCcost4 == 0:
            print ('Based on your inputs, unless you are willing/able to work more weekend days, this daycare option is unfortunatley not affordable for your current wages.')
        elif DCcost2 == 0 and DCcost3 == 0:
            print ('Based on your inputs, unless you are willing/able to work more weekend days, this daycare option is unfortunatley not affordable for your current wages.')
        elif DCcost3 == 0 and DCcost4 == 0:
            print ('Based on your inputs, unless you are willing/able to work more weekend days, this daycare option is unfortunatley not affordable for your current wages.')
        elif DCcost4 == 0:
            print ('Based on your inputs, the least amount of days you would want to have your child(ren) attend daycare is 5 days per week.')
            print ('\n')
            print ('Unless you are willing/able to work more weekend days, having your child attend day care less than 5 days per week means that your income will suffer to a point that the cost of daycare would, lead to weekly financial losses.')
        else:
            print ('Based on your inputs, the least amount of days you would want to have your child(ren) attend daycare is 4 days per week.')
            print ('\n')
            print ('Unless you are willing/able to work more weekend days, having your child attend day care less than 4 days per week means that your income will suffer to a point that the cost of daycare would, indeed, lead to weekly financial losses.') 
    elif len(NegativeList) == 3:                                                #The user does not make enough money to support only 4 days at daycare. They need to work more than that
        if DCcost5 == 0:
            print ('Based on your inputs, I suggest either finding a different daycare that gives you more options, or working more weekend days (if possible).')
        else:
            print ('Based on your inputs, the least amount of days you would want to have your child(ren) attend daycare is 5 days per week.')
            print ('\n')
            print ('Unless you are willing/able to work more weekend days, having your child attend day care less than 5 days per week means that your income will suffer to a point that the cost of daycare would, indeed, lead to weekly financial losses.') 
    else:                                                                       #The user may not be able to afford daycare at all
        print ('Based on your inputs, unless you are willing/able to work more weekend days, this daycare option is unfortunatley not affordable for your current wages.')
    print ('\n')
    print ('To help with your decision, I have listed below the net cashflow outcomes (Total Wages - Total DayCare Costs) for each of your options holding all other things (other revenue streams, other expenses, etc.) constant.')
    print ('\n')
    print ('This is the average amount of income (rounded to the nearest dollar) you will have left over every month for each of your daycare options.')
    print ('NOTE: Negative numbers mean that you will, in fact, lose that amount of money every month with those options.')
    print ('\n')
    if Net2 == 0 and Net3 == 0 and Net4 == 0:                                   #Print out cash flow results depending on how many daycare options there are per week.
        print ('5 days per week = $' + str(Net5))
    elif Net2 == 0 and Net3 == 0 and Net5 == 0:
        print ('4 days per week = $' + str(Net4))
    elif Net2 == 0 and Net4 == 0 and Net5 == 0:
        print ('3 days per week = $' + str(Net3))
    elif Net3 == 0 and Net4 == 0 and Net5 == 0:
        print ('2 days per week = $' + str(Net2))
    elif Net2 == 0 and Net3 == 0:
        print ('4 days per week = $' + str(Net4))
        print ('5 days per week = $' + str(Net5))
    elif Net2 == 0 and Net4 == 0:
        print ('3 days per week = $' + str(Net3))
        print ('5 days per week = $' + str(Net5))
    elif Net3 == 0 and Net4 == 0:
        print ('2 days per week = $' + str(Net2))
        print ('5 days per week = $' + str(Net5))
    elif Net2 == 0 and Net5 == 0:
        print ('3 days per week = $' + str(Net3))
        print ('4 days per week = $' + str(Net4))
    elif Net3 == 0 and Net5 == 0:
        print ('2 days per week = $' + str(Net2))
        print ('4 days per week = $' + str(Net4))
    elif Net4 == 0 and Net5 == 0:
        print ('2 days per week = $' + str(Net2))
        print ('3 days per week = $' + str(Net3))
    elif Net5 == 0:
        print ('2 days per week = $' + str(Net2))
        print ('3 days per week = $' + str(Net3))
        print ('4 days per week = $' + str(Net4))
    elif Net4 == 0:
        print ('2 days per week = $' + str(Net2))
        print ('3 days per week = $' + str(Net3))
        print ('5 days per week = $' + str(Net5))
    elif Net3 == 0:
        print ('2 days per week = $' + str(Net2))
        print ('4 days per week = $' + str(Net4))
        print ('5 days per week = $' + str(Net5))
    elif Net2 == 0:
        print ('3 days per week = $' + str(Net3))
        print ('4 days per week = $' + str(Net4))
        print ('5 days per week = $' + str(Net5))
    else:
        print ('2 days per week = $' + str(Net2))
        print ('3 days per week = $' + str(Net3))
        print ('4 days per week = $' + str(Net4))
        print ('5 days per week = $' + str(Net5))
    print ('\n')
    print ('NOTES:')
    print (' - Since taxes vary across states/countries, the dollar calculations noted above ignore taxes. These are the amounts you can expect BEFORE paying any state or federal taxes.')
    print (' - This program is only applicable to people whose employer pays them an hourly wage. It is not applicable to salaried individuals.')
    print (' - This program assumes that you can work a full 8-hour shift while your child(ren) attend(s) daycare.')
    print (' - This program calculates OverTime based on a time and a half rate for all hours worked after a 40 hour work week.')
    print (' - This program assumes that you will have someone to watch your child on weekends if you choose to work.')
    print (' - Finally, this program is only meant to supply a datapoint in your decision making. Many factors should be weighed in your choice(s) for daycare.')
    print ('************************************************************************************************************************************************************')
    
MakeUpYourMind()
