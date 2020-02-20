### MADmind, LLC.
### CSV Word Count Program
### v1 2/20/2020

import csv

def GetHeaderRow():
    'Opens file, reads header row, and closes the file'
    infile = open(r"<<INSERT FILE NAME HERE>>.csv")   #Insert the file name here. Be sure to include the extension. It must be a .csv format
    header = infile.readline()
    infile.close()
    return header

def FindAnswerIndex(Variable):
    'Finds the variable in the header of the file and returns the index of the variable'
    header = GetHeaderRow().split(',')
    index = header.index(Variable)
    return index    

def GetAnswerList(Variable):
    'Returns a list of only the variables the user cares about analyzing'
    AnsList = []
    SplitList = []
    index = FindAnswerIndex(Variable)                   #Index of varialbe the user is interested in analyzing
    with open('<<INSERT FILE NAME HERE>>.csv') as f:    #Insert file name here again
        reader = csv.reader(f)
        for row in reader:
            AnsList.append(row[index])
    for i in AnsList:
        SplitList.append(i.split())
    return SplitList

def GetAnsWords(Variable):
    'Returns a hashtable with word counts'
    HashTable = {}
    BadList = ['example1', 'example2', 'etc.']          #Add words here that you do not care about (e.g., 'and', 'the'). Must be in quotes ('')
    for word in BadList:
        badlist.append(word.lower())
    SplitList = GetAnswerList(Variable)
    for List in SplitList:
        for word in List:
            if word.lower() not in badlist:             #Counts words in list that are NOT in the "bad list"
                if word.lower() not in HashTable:
                    HashTable[word.lower()] = 1
                else:
                    HashTable[word.lower()] += 1
    return HashTable

def GetCount(Variable):                                 #When executing the program, simply type GetCount(Variable). Make sure you type the variable exactly
    'Prints the most common words of the variable you wish to assess'#how it shows up in the column header that you want to analyze and wrap it in quotes
    AnsDict = GetAnsWords(Variable)
    TuplesList = sorted(AnsDict.items(), reverse = True, key = lambda x: x[1])  #Sorts the hashtable on values in descending order
    NewList = []
    for i in TuplesList:
        NewList.append((i[0], i[1]))
    for t in NewList[:20]:          #Only returns the top 20 most common words from hashtable. Insert a different number if you want a longer/shorter list
        print (t)
