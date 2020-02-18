# PyElections
## Problem Statement
This challenge addresses the problem of helping the city of Houston modernize its vote-counting process for the next mayoral elections. No candidate won a majority (over 50%) of the vote during the general election that took place on November 5, 2019. The 2019 Houston mayoral election was decided by a runoff on December 14, 2019 to elect the Mayor of Space City. 
The scope of this project was to write a script that will decide the two candidates with the highest number of votes who will advance to the runoff election. 

# PyPoll Solution

* Given a set of the last general election data called houston_election_data.csv. The Candidate data is read into a dictionary using the candidate name as key, and the total votes as the value.  Although County and Voter ID data are provided they are not necessary to realize the solution.
* As each row is read in from the file it is used to build a dictionary containing unique key -> value pairs, where the key is the candidate name and the value is the accumulation of votes.  If the dictionary does not contain the candidate they are added with a value of 1 (votes).  If the dictionary does contain the candidate the value (vote) is incremented by 1. 
* The dictionary is then sorted by values (votes) and prined as follows: 
	* The total number of votes cast
	* A complete list of candidates who received votes
	* The percentage of votes each candidate won
	* The total number of votes each candidate won
* In additon the names of the two candidates who will advance to the runoff election are printed. 
* Election data is printed to both the terminal and to a text file. 
	*Data is written to an output file, if the file exists it is overwritten, otherwise a new file is created. 


# PyFinances

* Still within the `print_percentages()` function, create a conditional that checks a wrestler's loss percentage and prints either "Jobber" to the screen if the number was greater than fifty or "Superstar" if the number was less than 50.

