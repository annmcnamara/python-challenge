# The dataset is composed of three columns: 
# Candidate, County, and Voter ID. 
# Your task is to create a Python script that analyzes 
# the votes and calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# Print the names of the two candidates who will 
# advance to the runoff election.

# ASK ABUOT DIRECTORYpwd

import csv

#declare variables
Candidate = []      #array to hold Candidate Name
County = []         #array to hold County Name
VoterID = []        #array to hold VoterID

numVotes = []

headerRow = True
#read each row into sepaparte array
with open('houstonElection.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if (headerRow):
            headerRow = False
        else:
        #print(row)
        #print(row[0] + " " + row[1])  #for debugging
            Candidate.append(row[0])
           

uniqueCandidates = []
for i in range (0,len(Candidate)):
    #print(Candidate[i])
    if(Candidate[i] not in uniqueCandidates):
        #print (f"{Candidate[i]} not in there")
        uniqueCandidates.append(Candidate[i])

totalVotes = len(Candidate)

#print(f"{uniqueCandidates[0]}: {Candidate.count(uniqueCandidates[0])/totalVotes} ({Candidate.count(uniqueCandidates[0])})")

#print(f"Total Cast Votes {totalVotes}")

for  i in range (0, len(uniqueCandidates)):
#     print(Candidate.count(uniqueCandidates[i]))
    #print(f"{uniqueCandidates[i]}: {Candidate.count(uniqueCandidates[i])/totalVotes} ({Candidate.count(uniqueCandidates[i])})")
    numVotes.append(Candidate.count(uniqueCandidates[i]))
  

print("\nHouston Mayoral Election Results ")
print("----------------------------------------- ")
print(f"Total Cast Votes:{totalVotes}")
print("----------------------------------------- ")

#print("+++++++++++++++++++++++++++++++++++")
numVotes, uniqueCandidates = zip(*sorted(zip(numVotes, uniqueCandidates), reverse=True))
#print("\n\n",numVotes)
#print(uniqueCandidates)

for  i in range (0, len(uniqueCandidates)):
    print(f"{uniqueCandidates[i]}: {str(round(Candidate.count(uniqueCandidates[i])/totalVotes*100,2))} ({Candidate.count(uniqueCandidates[i])})")


# In a run off the two candidates with the most 
# votes proceed to a second round, 
print("-----------------------------------------")
print(f"1st Advancing Candidate: {uniqueCandidates[0]}")
print(f"2nd Advancing Candidate: {uniqueCandidates[1]}")
print("-----------------------------------------")


# print(len(Candidate))
# print(Candidate.count("Sylvester Turner")/len(Candidate))
# print(Candidate.count("Tony Buzbee")/len(Candidate))
# print(Candidate.count("Bill King")/len(Candidate))
# print(Candidate.count("Dwight A. Boykins")/len(Candidate))
# print(Candidate.count("Victoria Romero")/len(Candidate))
# print(Candidate.count("Victoria Romero")/len(Candidate))
# print(Candidate.count("Victoria Romero")/len(Candidate))


# # Houston Mayoral Election Results
# -----------------------------------------
# Total Cast Votes: 241032
# -----------------------------------------
# Sylvester Turner: 46.38% (111789)
# Tony Buzbee: 28.78% (69361)
# Bill King: 14.01% (33772)
# Dwight A. Boykins: 5.90% (14212)
# Victoria Romero: 1.22% (2933)
# Sue Lovell: 1.22% (2932)
# Demetria Smith: 0.70% (1694)
# Roy J. Vasquez: 0.65% (1556)
# Kendall Baker: 0.41% (982)
# Derrick Broze: 0.28% (686)
# Naoufal Houjami: 0.23% (560)
# Johnny “J.T.” Taylor: 0.23% (555)
# -----------------------------------------
# 1st Advancing Candidate: Sylvester Turner
# 2nd Advancing Candidate: Tony Buzbee
# -----------------------------------------

