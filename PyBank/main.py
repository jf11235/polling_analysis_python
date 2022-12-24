import os 
import csv

date = []
profloss = []
budgetDict = {}

budget_csv = os.path.join("/Users/joshuafeinberg/Documents/U-of-O-Bootcamp/Bootcamp_Class_Folder/Module_Challenges/Module 3 Challange/PyBank/Resources/budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        date.append(row[0])
        profloss.append(row[1])
    dataLen = len(date)
    print ("This data set has " + str(len(date)) + " months.") 



    def difference(x,y):
        return y-x

    


