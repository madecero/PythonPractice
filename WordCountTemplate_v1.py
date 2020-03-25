### MADmen, LLC.
### CSV Word Count Program
### v1 3/24/2020

import csv

def GetHeaderRow():
    'Opens file, reads header row, and closes the file'
    with open('<ENTER FILE NAME HERE>.csv') as f:
        FirstLine = f.readline().strip()                #Opens file and splits each row into an entry in a list
        f.close()                                       #Always close your files!
    return FirstLine

def FindAnswerIndex(Variable):
    'Finds the variable in the header of the file and returns the index of the variable'
    HeaderRow = GetHeaderRow()                          #Bring in first row of file
    Headers = HeaderRow.split(',')                      #Split first row into its seperate attributes (column headers)
    index = Headers.index(Variable)                     #Will index to match whichever column header the user is interested in analyzing
    return index    

def GetAnswerList(Variable):
    'Returns a list of only the variables the user cares about analyzing'
    AnsList = []
    SplitList = []
    index = FindAnswerIndex(Variable)                   #Index of variable the user is interested in analyzing
    with open('<ENTER FILE NAME HERE>.csv') as f:
        reader = csv.reader(f)                          #Reads in file row by row
        for row in reader:
            AnsList.append(row[index])                  #For each row, append only the contents of the cell under the column header in question
        f.close()
    for i in AnsList:
        SplitList.append(i.split())                     #For each entry in AnsList, split each word up to count later
    return SplitList

def GetAnsWords(Variable):
    'Returns a hashtable with word counts'
    HashTable = {}                                      #Empty hashtable for later. BadList = words we do not care about
    BadList = ['example1', 'example2', 'etc.']          #Enter words you want to exclude from count
    badlist = []                                        #Another empty "badlist" to append the words as all lowercase for comparison purposes
    for word in BadList:
        badlist.append(word.lower())
    SplitList = GetAnswerList(Variable)                 #Bring in entries of the variable (column header) in question
    for List in SplitList:
        for word in List:
            if word.lower() not in badlist:
                if word.lower() not in HashTable:
                    HashTable[word.lower()] = 1         #If word is not in bad list and it is not already counted in hashtable, have it = 1
                else:
                    HashTable[word.lower()] += 1        #If word is already in hashtable, add another count of 1
    return HashTable

def GetCount(Variable):
    'Prints the top 20 most common words'
    AnsDict = GetAnsWords(Variable)                     #Bring in all the words and their counts under the variable in question
    TuplesList = sorted(AnsDict.items(), reverse = True, key = lambda x: x[1])  #Sorts the hashtable on values in descending order
    NewList = []                                        #Following 3 lines will put the answer counts in descending order
    for i in TuplesList:
        NewList.append((i[0], i[1]))
    for t in NewList[:20]:                              #Only returns the top 20 most common words from hashtable
        print (t)
