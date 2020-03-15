### MADmind, LLC.
### Make Up Your Mind_COVID-19
### v1 3/15/2020

AcceptList = ['Y', 'N']

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
    print ("It sounds like you need help deciding whether or not to get tested for COVID-19 (CoronaVirus). First, let's get some information from you.")
    TempList = GetTemp()                        #Asks user what his or her current temperature is
    Cough = GetCough()                          #Asks user if he or she has a cough and/or shortness of breath
    Visits = GetVisits()                        #Asks user which countries they have been to in the past 14 days
    Contact = GetContact()                      #Asks user if they have had contact with a confirmed COVID patient in the past 14 days
    Rec = DetermineTest(TempList, Cough, Visits, Contact) #Gives user recommendation on if he or she should get tested for COVID-19 based on inputs
    print ('\n')
    print ('Thank you for visiting MADmind. I hope to see you again soon!')

def GetTemp():
    'Function that asks user what his or her current temperature is'
    print ('\n')
    while True:                                 #First ask user if he or she has access to a thermometer
        try:
            Therm = eval(input("Do you have access to a thermometer to take your temperature? Please enter either 'Y' or 'N' in quotes (''): "))
        except:
            print("Please only enter either 'Y' or 'N' in quotes (''). ")
            continue                            #better try again... Return to the start of the loop
        else:
            break                               #it worked! we're ready to exit the loop.
    while Therm.upper() not in AcceptList:
        print("Please only enter either 'Y' or 'N' in quotes (''). ")
        while True:
            try:
                Therm = eval(input("Do you have access to a thermometer to take your temperature? Please enter either 'Y' or 'N' in quotes (''): "))
            except:
                print("Please enter either 'Y' or 'N' in quotes ('').")
                continue                        #better try again... Return to the start of the loop
            else:
                break                           #it worked! we're ready to exit the loop.
    if Therm.upper() == 'Y':
        print ('\n')
        while True:                             #if user has access to thermometer, ask him or her what their current temperature is
            try:
                Degrees = eval(input("Please enter your current temperature (including the decimal point) in degrees Fahrenheit: "))
            except:
                print("Please enter a number and only a number (including the decimal point).")
                continue                        #better try again... Return to the start of the loop
            else:
                break                           #it worked! we're ready to exit the loop.
        while type(Degrees) is not float:
            print("Please enter a number and only a number (including the decimal point).")
            while True:
                try:
                    Degrees = eval(input("Please enter your current temerature (including the decimal point) in degrees Fahrenheit: "))
                except:
                    print("Please enter a number and only a number (including the decimal point).")
                    continue                    #better try again... Return to the start of the loop
                else:
                    break                       #it worked! we're ready to exit the loop.
    else:                                       #If user does not have access to thermometer, ignore the entry regarding fever
        Degrees = 0
    if Degrees >= 100.4:                        #Best practice says a true fever is greater than 100.4 degrees ferenheit
        Temp = 'Y'
    else:
        Temp = 'N'
    TempList = [Temp, Therm]
    return TempList

def GetCough():
    'Function that asks user if he or she has a cough and/or shortness of breath'
    print ('\n')
    while True:
        try:
            Cough = eval(input("Are you currently experiencing a cough and/or shortness of breath? Please enter either 'Y' or 'N' in quotes (''): "))
        except:
            print("Please enter either 'Y' or 'N' in quotes ('').")
            continue                            #better try again... Return to the start of the loop
        else:
            break                               #it worked! we're ready to exit the loop.
    while Cough.upper() not in AcceptList:
        print("Please enter either 'Y' or 'N' in quotes ('').")
        while True:
            try:
                Cough = eval(input("Are you currently experiencing a cough and/or shortness of breath? Please enter either 'Y' or 'N' in quotes (''): "))
            except:
                print("Please enter either 'Y' or 'N' in quotes ('').")
                continue                        #better try again... Return to the start of the loop
            else:
                break                           #it worked! we're ready to exit the loop.
    return Cough

def GetVisits():
    'Function that asks user which countries they have been to in the past 14 days'
    print ('\n')
    print ('Have you been to any of the following countries in the past 14 days?')
    print ('China, Japan, South Korea, Iran, Italy')
    print ('\n')
    while True:                                 #First ask user if he or she has been out of the country in the past 14 days
        try:
            Visits = eval(input("Please enter either 'Y' or 'N' in quotes (''): "))
        except:
            continue                            #better try again... Return to the start of the loop
        else:
            break                               #it worked! we're ready to exit the loop.
    while Visits.upper() not in AcceptList:
        while True:
            try:
                Visits = eval(input("Please enter either 'Y' or 'N' in quotes (''): "))
            except:
                continue                        #better try again... Return to the start of the loop
            else:
                break                           #it worked! we're ready to exit the loop.
    return Visits

def GetContact():
    'Function that asks user if they have had contact with a confirmed COVID patient in the past 14 days'
    print ('\n')
    while True:
        try:
            Contact = eval(input("Have you had phyiscal contact with a laboratory confirmed COVID-19 patient within the past 14 days? Please enter either 'Y' or 'N' in quotes (''): "))
        except:
            print("Please enter either 'Y' or 'N' in quotes ('').")
            continue                            #better try again... Return to the start of the loop
        else:
            break                               #it worked! we're ready to exit the loop.
    while Contact.upper() not in AcceptList:
        print("Please enter either 'Y' or 'N' in quotes ('').")
        while True:
            try:
                Contact = eval(input("Have you had phyiscal contact with a laboratory confirmed COVID-19 patient within the past 14 days? Please enter either 'Y' or 'N' in quotes (''): "))
            except:
                print("Please enter either 'Y' or 'N' in quotes ('').")
                continue                        #better try again... Return to the start of the loop
            else:
                break                           #it worked! we're ready to exit the loop.
    return Contact

def DetermineTest(TempList, Cough, Visits, Contact):
    'Function that gives user recommendation on if he or she should get tested for COVID-19 based on inputs'
    Fever = TempList[0]
    Therm = TempList[1]
    FeverCoughList = [Fever.upper(), Cough.upper()]
    ContactList = [Visits.upper(), Contact.upper()]
    SevereAnswer = 'You should get tested for COVID-19 (CoronaVirus). Call your primary care provider for further instruction.'
    LowRiskAnswer = 'You are at low risk of having COVID-19 (CoronaVirus). Stay home. Do not got to work. Continue to take your temperature, and call your primary care provider for further instructions.'
    NoThermAnswer = 'You are currently at low risk of COVID-19 (CoronaVirus), but you should take your temperature. Call your primary care provider for further instruction.'
    NoRiskAnswer = 'You are currently at low risk of COVID-19 (CoronaVirus). If you feel ill, stay home. Do not go to work. Call your primary care provider if you have questions or concerns.'
    print ('\n')
    print ('************************************************************************************************************************************************************')
    print ('\n')
    if 'Y' in FeverCoughList and 'Y' in ContactList:
        print (SevereAnswer)                    #If user has a fever and has either been to an at risk country or has been in cantact with a known patient, he or she may need to get tested
    elif Fever.upper() == 'Y' and Cough.upper() == 'Y':
        print (LowRiskAnswer)                   #If user has both a fever and a cough (and/or shortness of breath), but he or she has not been in contact with a patient nor has been to an at risk country, he or she does not need to be tested
    elif 'Y' in ContactList and Therm.upper() == 'N':
        print (NoThermAnswer)                   #If user has been to an at risk country and/or been in contact with a known patient, but does not have a thermometer, and he or she does not have a cough, they should contact their primary care provider
    else:
        print (NoRiskAnswer)                    #User does not have symptoms, so he or she does not need to get tested
    print ('\n') 
    print ('NOTE:')
    print ('This algorithm is based on public health guidelines (URL below) as of 3/13/2020. It is not meant to be a test of or for COVID-19 (CoronaVirus). You should contact your primary care provider if you have any questions or concerns.')
    print ('http://www.dph.illinois.gov/topics-services/diseases-and-conditions/diseases-a-z-list/coronavirus/health-care-providers/PUI-decision-matrix')
    print ('\n')
    print ('************************************************************************************************************************************************************')
    
MakeUpYourMind()
