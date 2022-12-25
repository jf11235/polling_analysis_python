import os
import csv





#making a function to print to terminal and write to text file in one line
def print_to_terminal_and_file(f, *args, **kwargs):
    return print(*args, **kwargs), print(*args, file=f, **kwargs)


electionCSV = os.path.join(/Users/joshuafeinberg/Documents/python-challenge/PyPoll/Resources/election_data.csv)

with open(electionCSV) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:





#output_file = os.path.join("/Users/joshuafeinberg/Documents/python-challenge/PyPoll/analysis/PyPollanalysis.md")
#writing outcomes to csv file
#with open(output_file,"w") as datafile:

    
