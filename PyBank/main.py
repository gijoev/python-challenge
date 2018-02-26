# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 05:02:33 2018

@author: gjvarkey
"""
import os
import csv

pybank_csvpath = os.path.join("../PyBank","budget_data_1.csv")

#initialize variables and lists
months = 0 
monthlyRevenue= 0
minRevMonth = 0
maxRevMonth = 0
revenue = 0
totalRevenue = 0 
averageChange = 0
totalRevenueChange = 0
prevRevenue = monthlyRevenue
dates = []
amount = []
avgRevChange = []
grtInc = []
grtDec = []

with open(pybank_csvpath, 'r', newline='') as csvFile:
    csvreader = csv.reader(csvFile, delimiter= ',')
    # skip header row
    next(csvreader)
    
    for row in csvreader:
        revenue = row[1]
        #months.append(row[0])
        months = months + 1
        #revenue.append(row[1])
        monthlyRevenue = monthlyRevenue + int(row[1])
        #averageChange.append(row[2])
        percent = round(int(row[1]) / int(row[1]), 2)
        totalRevenue = float(revenue) + float(row[1])
        averageChange = (int(row[1])/int(row[1]))
        if monthlyRevenue > 1:
            averageChange = int(monthlyRevenue) - prevRevenue
            totalRevenueChange = totalRevenueChange + averageChange
            if float(totalRevenue) > float(maxRevMonth):
                grtIncChange = totalRevenueChange
                maxRevMonth = months
                if float(totalRevenue) < float(minRevMonth):
                    grtDecChange = totalRevenueChange
                    minRevMonth = months
                    #review_percent.append(percent)
                    revChange = totalRevenueChange
                    dates.append(row[0])
                    amount.append(row[1])
                    avgRevChange.append(revChange)
                    grtInc.append(grtIncChange, maxRevMonth)
                    grtDec.append(grtDecChange, minRevMonth)

#zip and print lists
budget_csv = list(zip(dates, amount, avgRevChange, grtInc, grtDec))
print(budget_csv)
# Set variable for output file
output_file = os.path.join("../PyBank", "Budget_Analysis.txt")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Total Months", "Total Revenue", "Average Revenue Change", "Greatest Increase in Revenue", "Greatest Decrease in Revenue"])
# Write in zipped rows
writer.writerows(budget_csv)