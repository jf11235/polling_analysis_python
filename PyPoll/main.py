import os
import csv

ballotID = []
county = []
candidates = []
candiDict ={}



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
    print(f"Total votes: {len(ballotID)}")
    #print_to_terminal_and_file(datafile, f"Total votes: {len(ballotID)}")

    print("-------------------------")

    for candidate in candidates:
        if candidate[i] != candidate[i+1]:
            


    





#output_file = os.path.join("/Users/joshuafeinberg/Documents/python-challenge/PyPoll/analysis/PyPollanalysis.md")
#writing outcomes to csv file
#with open(output_file,"w") as datafile:


