# Python script that reads in csv file then analyzes the records 
# to calculate each of the following:
# 
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv



def countUnique(theArray): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in theArray: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return len(unique_list)

csvpath = os.path.join('.', 'budget_data.csv')


#declare variables
#profitLoss = [] #array to hold profit and loss data
dates = []      #arry to hold dates
d = {}
# headerRow = True
# #read each row into sepaparte array
# with open('budget.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         if (headerRow):
#             headerRow = False
#         else:
#         #print(row)
#         #print(row[0] + " " + row[1])  #for debugging
#             profitLoss.append(int(row[0]))
#             dates.append(row[1])

# changes = []
# numberOfRows = len(profitLoss)


with open(csvpath) as csvfile:
      readCSV = csv.DictReader(csvfile, delimiter=',')
      for row in readCSV:
        if row['Date'] not in d:  # add the candidate to the dictionary
            d[row['Date']] =  float(row['Profit/Losses'])  #set candidate votes to 1
        else: ## add one
            d[row['Date']] += 1     # if they are already in the dictionary 
                                       # increment vote total by 1
   
totalMonths = len(d)
profitLoss = sum(d.values())

mylist = []
changes = []
for key, value in d.items():
    dates.append(key)
    mylist.append(value)

print(mylist[0])

for i in range(0, totalMonths-1):
    changes.append(mylist[i+1] - mylist[i])


average_change = sum(changes)/(totalMonths-1)

greatestIncrease = max(changes)
greatestDecrease = min(changes)

print(greatestIncrease)
print(greatestDecrease)


minIndex = changes.index(greatestDecrease)
maxIndex = changes.index(greatestIncrease)

print(" ")
print("Financial Analysis")
print("----------------------------")
print("Total Months: ", totalMonths)
print(f"Total:   ${profitLoss:2.0f}")
print(f"Average Change: ${average_change:2.2f}")
print(f"Greatest Increase in Profits: {dates[maxIndex+1]} (${greatestIncrease:2.0f}) ")
print(f"Greatest Decrease in Profits: {dates[minIndex+1]} (${greatestDecrease:2.0f}) ")


# # The average of the changes in "Profit/Losses" over the entire period
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)



