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
import sys  # I need this because I wanted std out and wrote a function to print results

def printResults(toLocation):
    # function to print results
    # takes an output stream as a parameter called toLocation
    # toLocation is either standard output or a filename reference
    toLocation.write("Financial Analysis \n")
    toLocation.write("----------------------------\n")
    toLocation.write(f"Total Months: {totalMonths}\n")
    toLocation.write(f"Total:   ${profitLoss:2.0f}\n")
    toLocation.write(f"Average Change: ${average_change:2.2f}\n")
    toLocation.write(f"Greatest Increase in Profits: {dates[maxIndex+1]} (${greatestIncrease:2.0f})\n")
    toLocation.write(f"Greatest Decrease in Profits: {dates[minIndex+1]} (${greatestDecrease:2.0f})\n")

# Createmake references to paths for reading and writing files
csvpath = os.path.join('.','Resources', 'budget_data.csv')  #input file
txt_output_path = os.path.join(".", "budget_results.txt")   # output file

#declare and initialize variables
dates = []          # array to hold dates
profitOrLoss = []   # set up an empty array to hold the individual values
changes = []        # Array to hold increase/decrease from month to month

totalMonths = 0     # A variable to hold the number of months, initialized to 0

fileExists = os.path.isfile(csvpath) # Check if the file exists - this returns True/False
if(fileExists):  # The file exists, continue with processing the data
    totalVotes = 0      #holds total votes, initialize to 0
 
    #read each row populating two arrays with dates and profit/losses
    #and accumulating the number of months

    with open(csvpath) as csvfile:
      readCSV = csv.reader(csvfile, delimiter=',')  
      headers = next(readCSV)   # clear the header row
      for row in readCSV:       # for each row
          totalMonths += 1      # keep a running total of the number of months
          #populate two arrays using the read in data
          dates.append(row[1])
          profitOrLoss.append(float(row[0]))

    # Sum all profit and loss
    profitLoss = sum(profitOrLoss)    #sum all the amounts for total profit/loss

    #populate a changes array with the differences in profit and loss from month to month
    for i in range(0, totalMonths-1):   #array runs from 0 to n-1
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

    # Output results to the screen 
    # I wrote a function to do this just to practice
    # the function accepts a single pararmeter that holds where to output the data
    printResults(sys.stdout)  #pass standard output

    # Output the results to a file
    # after first checking if it exist to determine the mode to open the file
    # If the file exists it is opened for write and overwritten
    # otherwise a new file is created
    writeFileExists = os.path.isfile(txt_output_path)
    # set the open mode accordingly
    openMode = 'w'              # Set the mode to write by defauld
    if not (writeFileExists):   # if the file doesnt exist
        openMode = 'x'          # then set the mode to "exclusive creation"
                                # a new file will be created if it doesnt exist
    with open(txt_output_path, openMode) as outputFile: #open the file
          printResults(outputFile)  #pass output file handle

else: # The input file does not exist 
      # output an error message
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



