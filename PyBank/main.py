# main.py
# Ann McNamara, February 2020

# Python script that reads in csv file then analyzes the records 
# to calculate each of the following:
# 
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

#import dependancies
import os
import csv
import sys

def printResults(toLocation):
    ##function to print results
    ##takes output stream as a parameter called toLocation
    #toLocation is either standard output or a filename reference
    toLocation.write("Financial Analysis \n")
    toLocation.write("----------------------------\n")
    toLocation.write(f"Total Months: {totalMonths}\n")
    toLocation.write(f"Total:   ${profitLoss:2.0f}\n")
    toLocation.write(f"Average Change: ${average_change:2.2f}\n")
    toLocation.write(f"Greatest Increase in Profits: {dates[maxIndex+1]} (${greatestIncrease:2.0f})\n")
    toLocation.write(f"Greatest Decrease in Profits: {dates[minIndex+1]} (${greatestDecrease:2.0f})\n")

#make references to paths for reading and writing files
csvpath = os.path.join('.','Resources', 'budget_data.csv')              #input file
txt_output_path = os.path.join(".", "budget_results.txt")   # output file

#declare and initialize variables
dates = []          #array to hold uniquedates
d = {}              #dictionary to hold key, value (date, amount) pairs
profitOrLoss = []   #set up an empty array to hold the individual values
changes = []        #Array to hold increase/decrease from month to month

fileExists = os.path.isfile(csvpath) 
if(fileExists):  #process the file
    totalVotes = 0      #holds total votes, initialize to 0
    d = {}              #candidate dictionary.  
                        # Key is candidate name, 
                        # value is populated with accumulated votes

    #read each row populating the dictionary with unique candidate names
    #and accumulating the number of votes

    with open(csvpath) as csvfile:
      readCSV = csv.DictReader(csvfile, delimiter=',')
      for row in readCSV:
        if row['Date'] not in d:  # add the candidate to the dictionary
            d[row['Date']] =  float(row['Profit/Losses'])  #set candidate votes to 1
        else: ## add one
            d[row['Date']] += 1     # if they are already in the dictionary 
                                       # increment vote total by 1
   
    totalMonths = len(d)    #set the total month to the length of the dictionary
    profitLoss = sum(d.values())    #set profitLoss to the sum of all teh values

    #break out the dictionary into two arrays for computation
    for key, value in d.items():
      dates.append(key)
      profitOrLoss.append(value)

    #populate the changes array with the differences in profit and loss from month to month
    for i in range(0, totalMonths-1):
        changes.append(profitOrLoss[i+1] - profitOrLoss[i])
   
    #calculate the average change
    average_change = sum(changes)/len(changes)

    #use built in functions min and max to find the greatest increase and greatest decrease
    greatestIncrease = max(changes)
    greatestDecrease = min(changes)

    #use built in functions index to find the index for greatest increase and greatest decrease
    #This index will be used to get the date for the greatest increase and greatest decrease
    minIndex = changes.index(greatestDecrease)
    maxIndex = changes.index(greatestIncrease)

    #output results to the screen
    #I wrote a function to do this just to practice
    #the function accepts a single pararmeter that holds where to output the data
    printResults(sys.stdout)  #pass standard output

    #output the results to a file
    #after first checking if it exist to determine the mode to open the file
    #If the file exists it is opened for write and overwritten
    #otherwise a new file is created
    writeFileExists = os.path.isfile(txt_output_path)
    #set the open mode accordingly
    openMode = 'w'  #set the mode to write
    if not (writeFileExists):   #if the file doesnt exist
        openMode = 'x'          #then set the mode to "exclusive creation"
                                # a new file will be created if it doesnt exist
    with open(txt_output_path, openMode) as outputFile:
          printResults(outputFile)  #pass output file handle

else: #the input file does not exist
    #output an error message
    print(f"ERROR: INPUT FILE {csvpath} does not exist, please check your path and filename")

# SAMPLE OUTPUT
# # The average of the changes in "Profit/Losses" over the entire period
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)



