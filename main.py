# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:30:29 2018

@author: gjvarkey
"""

import os
import csv

csvFile = os.path.join("raw_data","election_data_1.csv")

totalVotes = 0
poll = {}
candidateList = []
voteCountPerCandidate = []
votePercentage = []
winner = []


with open (csvFile, newline ="") as cfile:
    reader = csv.reader(cfile, delimiter=",")
    next (reader)
    
    for row in reader:
        totalVotes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
    for i,j in poll.items():
        candidateList.append(i)
        voteCountPerCandidate.append(j)
    #print(candidateList)
    #print(voteCountPerCandidate)
    
    for num in voteCountPerCandidate:
        votePercentage.append(round(num/totalVotes*100,1))
    #print(votePercentage)
    
    combineLists = list(zip(candidateList, voteCountPerCandidate, votePercentage))
    #print(combineLists)
    
    for winnerName in combineLists:
        if max(voteCountPerCandidate) == winnerName[1]:
            winner.append(winnerName[0])
    #print(winner)
    winnerStr = winner[0]
    
    with open ("Results.txt", "w") as output:
        output.writelines("Election Results \n------------------------- \n")
        output.writelines("Total Votes: " + str(totalVotes) + "\n")
        output.writelines("------------------------- \n")
        for line in combineLists:
            output.writelines(str(line[0]) + ": " + str(line[2]) + "%" 
                              + " (" + str(line[1]) + ")\n" )
        output.writelines('------------------------- \nWinner: ' 
                          + winnerStr + '\n-------------------------')
    
    with open("Results.txt", "r") as readFile:
        print(readFile.read())