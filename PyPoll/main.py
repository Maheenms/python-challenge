"""
In this challenge, we are tasked with helping a small, rural town modernize its vote counting process.
We are given a set of poll data called election_data.csv. 
The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
Our task is to create a Python script that analyzes the votes and calculates each of the following:

1)The total number of votes cast
2)A complete list of candidates who received votes
3)The percentage of votes each candidate won
4)The total number of votes each candidate won
5)The winner of the election based on popular vote.

"""

#import the csv and os as modules
import os
import csv
 
 #Load the csv file to read the election data 
fileLoadPyPoll = os.path.join ("Resources","election_data.csv")

#To check if we have the correct path and folder
#print(fileLoad)

# Output file Location for the Election data Analysis/Creates the path and the text file (it will rewrite the text file {in write mode}if it already exists)
OutPutFile = os.path.join("Analysis","election_data_Analysis.txt")

# Declare your accumulator variables 
TotalVotesCast = 0 # Counter for the total number of votes cast
#Variable for a list that holds the candidates in the data
Candidates = []  
# Variable for a Dictionary that will hold the votes that each candidate receives
CandidateVotes = {} 
#variable to hold the winning count
WinningCounter = 0 
#Variable to hold the Winner Candidate
WinningCandidate = ""


#read the csv file
with open(fileLoadPyPoll)as election_data:
    #create the csv reader
    csvreader = csv.reader(election_data)


    #read the header and skip down to the next line
    header = next(csvreader)
    #print(header) #just to check if it prints the header 

    #rows will be lists 
       #index 0 is the Ballot ID 
       #index 1 is the User's Choice of Candidate
    

    #for  each row 
    for row in csvreader :
        #add on to the total votes
        TotalVotesCast += 1  #this is the same as TotalVotes =TotalVotes + 1
        
        #Check to see if the candidate is in the list of candidates
        if row[2] not in Candidates:
            # if not in the list then add it to the list of candidates
            Candidates.append(row[2])

            #add the value to the dictionary as well
            #{"Key" : Value}
            #start the counts at 1 for the votes
            CandidateVotes[row[2]] = 1

        else:
            # If the candidate is in the list of candidates 
            #Then add a vote to the candidates count
            CandidateVotes[row[2]] += 1

# To see the dictionary with the candidates and their votes               
#print(CandidateVotes)

Voter_Output = "" #empty string as we will increment it inside the for loop

for Candidates in CandidateVotes:
    # Get the votes for each candidate and their percentages
    Votes = CandidateVotes.get(Candidates) # pulling out the votes of each candidate in the dictionary
    #print(Votes) #Checking the Votes 
    VotesPercentage = (float(Votes)/ float(TotalVotesCast))*100
    #Output of all the candidates in the candidate list with their respective votes 
    Voter_Output += f"{Candidates}: {VotesPercentage:,.3f}%  ({Votes})\n"

    #display just to check the code for voter_ouput
    #print(Voter_Output)
 
    #Compare the votes to the winning count 
    if Votes > WinningCounter:
        #Update the votes to the new winning count
        WinningCounter = Votes
        #update the winning candidate
        WinningCandidate = Candidates


WinningCandidate_Output = f"Winner: {WinningCandidate}\n"
    

#create and output variable to hold the output 
OutPut = (
    f"Election Results\n"
    f"-----------------------------\n"
    f"Total Votes: {TotalVotesCast} \n" 
    f"-----------------------------\n"
    f"{Voter_Output}"
    f"-----------------------------\n"
    f"{WinningCandidate_Output}"
    f"-----------------------------\n"

) 

# Display output to console/terminal/gitbash
print(OutPut)

#display/print output in election data analysis text file 
with open(OutPutFile, "w") as textFile :
    #write the output to the text file
    textFile.write(OutPut)
