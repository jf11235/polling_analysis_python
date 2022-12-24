import os 
import csv

date = []
profloss = []
changes = []
#budgetDict = {}
total = 0



budget_csv = os.path.join("/Users/joshuafeinberg/Documents/U-of-O-Bootcamp/Bootcamp_Class_Folder/Module_Challenges/Module 3 Challange/PyBank/Resources/budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        date.append(row[0])
        profloss.append(row[1])
    date.pop(0)
    profloss.pop(0)
    dataLen = len(date)
    print ("This data set has " + str(len(date)) + " months.") 

    #print(date[0])
    #print(profloss[0])
    
    for i in range(0, len(profloss)):
        profloss[i] = int(profloss[i])
        total = total + (profloss[i])
        difference = (profloss[i+1]) - (profloss[i])
        changes.append(difference)
    print(changes[0])

    #print(f' The total profit/loss is ${total}')




    

    


