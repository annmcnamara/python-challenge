# Python script that reads in csv file then analyzes the records 
# to calculate each of the following:
# 
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

def countUnique(theArray): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in theArray: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return len(unique_list)

import csv

#declare variables
profitLoss = [] #array to hold profit and loss data
dates = []      #arry to hold dates

headerRow = True
#read each row into sepaparte array
with open('budget.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if (headerRow):
            headerRow = False
        else:
        #print(row)
        #print(row[0] + " " + row[1])  #for debugging
            profitLoss.append(int(row[0]))
            dates.append(row[1])

changes = []
numberOfRows = len(profitLoss)

#print(profitLoss)

for i in range (0, numberOfRows-1):
    #print(f"{profitLoss[i]} {profitLoss[i+1]} {profitLoss[i]-profitLoss[i+1]}")
    changes.append(profitLoss[i]-profitLoss[i+1])

#print(sum(changes))

greatestIncrease = max(changes)
greatestDecrease = min(changes)

minIndex = changes.index(greatestDecrease)
maxIndex = changes.index(greatestIncrease)

print(" ")
print("Financial Analysis")
print("----------------------------")
print("Total Months: ", countUnique(dates))
print("Total:   $" + str(sum(profitLoss)))
print("Average Change: $",sum(changes) / (numberOfRows-1))
print(f"Greatest Increase in Profits: {dates[maxIndex]} (${greatestIncrease})) ")
print(f"Greatest Decrease in Profits: {dates[minIndex]} (${greatestDecrease})) ")

# # The average of the changes in "Profit/Losses" over the entire period
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)



