import os
import csv

ballotID = []
county = []
candidates = []
eachCandidate = []
candiDict ={}
totalVotes = 0



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

    print("Election Results")
    print("-------------------------")

    #counting number of votes:
    totalVotes = len(ballotID)
    print(f"Total votes: {totalVotes}")
    #print_to_terminal_and_file(datafile, f"Total votes: {len(ballotID)}")

    print("-------------------------")
    #removes duplicates from candidates
    eachCandidate = set(candidates)
    #this doesnt work
    #candiDict = {eachCandidate[i]: totalVotes for i in range(len(candiDict))}
    

    for i in eachCandidate:
        candiDict[i] = candidates.count(i)

    print(candiDict)


        

    #for i in range(len(candidates)):
    #    if candidates[i] != candidates[i+1]:
    #        totalVotes += 1
            #candiDict = {candidates[i]: totalVotes}
    #        totalVotes = 0

    #    else:
    #        totalVotes += 1
            #candiDict = {candidates[i]: totalVotes}

    #print(candiDict)
    



    





#output_file = os.path.join("/Users/joshuafeinberg/Documents/python-challenge/PyPoll/analysis/PyPollanalysis.md")
#writing outcomes to csv file
#with open(output_file,"w") as datafile:
