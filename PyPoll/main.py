# main.py
# Ann McNamara, February 2020
# 
# The dataset is composed of three columns: 
# Candidate, County, and Voter ID. 
# This Python script analyzes 
# the votes and calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# Print the names of the two candidates who will 
# advance to the runoff election.

# Data is written to an output file.
# If the file exists it is overwritten
# otherwise ia new ouput file is is created

#import dependancies
import csv
import os

#make references to paths for reading and writing files
csvpath = os.path.join('.', 'Resources', 'houston_election_data.csv')  #input file
txt_output_path = os.path.join(".", "houston_election_results.txt")    #output file

# Check first that the input file exists
# if the file exists then continue with processing
# otherwise, the file is not found display an error mesage

fileExists = os.path.isfile(csvpath) 
if(fileExists):
    totalVotes = 0      #holds total votes, initialize to 0
    d = {}              #candidate dictionary.  
                        # Key is candidate name, 
                        # value is populated with accumulated votes

    # Read each row populating the dictionary with unique candidate names
    # as we go and accumulating the number of votes
    with open(csvpath) as csvfile:
      readCSV = csv.DictReader(csvfile, delimiter=',') #using DictReader takes care of headers
      for row in readCSV:              # As we read in each row
        if row['Candidate'] not in d:  # add the candidate to the dictionary
            d[row['Candidate']] = 1    #set candidate votes to 1
        else: ## add one
            d[row['Candidate']] += 1   # if they are already in the dictionary 
                                       # increment vote total by 1
    #end with

    #sum total votes
    totalVotes = sum(d.values())

    # Sort the dictionary on value using list comprehension
    # Note: this will flip the order of key and value
    sorted_d = sorted(((value, key) for (key,value) in d.items()), reverse=True)

    # Output formated results to the screen
    print("\nHouston Mayoral Election Results ")
    print("----------------------------------------- ")
    print(f"Total Cast Votes:{totalVotes}")
    print("----------------------------------------- ")

    for c in sorted_d:
     print(f"{c[1]}: {(c[0]/totalVotes)*100:2.2f}% ({c[0]}) ")

    # In a run off the two candidates with the most 
    # votes proceed to a second round
    # print formated results to the screen
    # As the dictionary is sorted by votes the first two rows represent the 
    # Advancing Candidates

    print("-----------------------------------------")
    print(f"1st Advancing Candidate: {sorted_d[0][1]}")
    print(f"2nd Advancing Candidate: {sorted_d[1][1]}")
    print("-----------------------------------------")

    # Print formated results to the a text file
    # First check if the file exists
    writeFileExists = os.path.isfile(txt_output_path)
    # Set the open mode accordingly
    openMode = 'w'              # Set the open mode to write by defauld
    if not (writeFileExists):   # If the file does not exist
        openMode = 'x'          # then set the open mode to creation
                                # otherwise it just stays as write mode
    with open(txt_output_path, openMode) as outputFile:
    #print formated results to a text file
        outputFile.write("\nHouston Mayoral Election Results \n")
        outputFile.write("----------------------------------------- \n")
        outputFile.write(f"Total Cast Votes:{totalVotes} \n")
        outputFile.write("----------------------------------------- \n")

        #loop through each value in the sorted dictionary
        for c in sorted_d:
            outputFile.write(f"{c[1]}: {(c[0]/totalVotes)*100:2.2f}% ({c[0]}) \n")

        #output the run off candidates
        outputFile.write("----------------------------------------- \n")
        outputFile.write(f"1st Advancing Candidate: {sorted_d[0][1]} \n")
        outputFile.write(f"2nd Advancing Candidate: {sorted_d[1][1]} \n")
        outputFile.write("----------------------------------------- \n")
    # end with
else: #the input file does not exist
    print(f"ERROR: INPUT FILE {csvpath} does not exist, please check your path and filename")

# # SAMPLE OUTPUT
# # # Houston Mayoral Election Results
# # -----------------------------------------
# # Total Cast Votes: 241032
# # -----------------------------------------
# # Sylvester Turner: 46.38% (111789)
# # Tony Buzbee: 28.78% (69361)
# # Bill King: 14.01% (33772)
# # Dwight A. Boykins: 5.90% (14212)
# # Victoria Romero: 1.22% (2933)
# # Sue Lovell: 1.22% (2932)
# # Demetria Smith: 0.70% (1694)
# # Roy J. Vasquez: 0.65% (1556)
# # Kendall Baker: 0.41% (982)
# # Derrick Broze: 0.28% (686)
# # Naoufal Houjami: 0.23% (560)
# # Johnny “J.T.” Taylor: 0.23% (555)
# # -----------------------------------------
# # 1st Advancing Candidate: Sylvester Turner
# # 2nd Advancing Candidate: Tony Buzbee
# # -----------------------------------------

