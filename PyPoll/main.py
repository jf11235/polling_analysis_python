import os
import csv

ballotID = []
county = []
candidates = []
eachCandidate = []
candiDict ={}
candiPerc = {}
totalVotes = 0
doaneVotePer = 0
stockhamVotePer = 0
degetteVotePer = 0


#making a function to print to terminal and write to text file in one line
def print_to_terminal_and_file(f, *args, **kwargs):
    return print(*args, **kwargs), print(*args, file=f, **kwargs)


electionCSV = os.path.join("/Users/joshuafeinberg/Documents/python-challenge/PyPoll/Resources/election_data.csv")

with open(electionCSV) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")



   
#seperating the columns into 3 lists
    for row in csvreader:
        ballotID.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    #removing headers
    ballotID.pop(0)
    county.pop(0)
    candidates.pop(0)
    
#output_file = os.path.join("/Users/joshuafeinberg/Documents/python-challenge/PyPoll/analysis/PyPollanalysis.md")
#writing outcomes to csv file
#with open(output_file,"w") as datafile:

    print("Election Results")
    print("-------------------------")

    #counting number of votes:
    totalVotes = len(ballotID)
    print(f"Total votes: {totalVotes}")
    #print_to_terminal_and_file(datafile, f"Total votes: {len(ballotID)}")

    print("-------------------------")
    #removes duplicates from candidates
    eachCandidate = set(candidates)
    
    
    #creating a dictionary keys = candidates, values = vote count
    for i in eachCandidate:
        candiDict[i] = candidates.count(i)

    
    doaneVotePer = candiDict ["Raymon Anthony Doane"]/totalVotes
    stockhamVotePer = candiDict ["Charles Casper Stockham"]/totalVotes
    degetteVotePer = candiDict ["Diana DeGette"]/totalVotes

    



    





#output_file = os.path.join("/Users/joshuafeinberg/Documents/python-challenge/PyPoll/analysis/PyPollanalysis.md")
#writing outcomes to csv file
#with open(output_file,"w") as datafile:
