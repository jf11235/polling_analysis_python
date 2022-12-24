import os 
import csv

date = []
profloss = []
changes = []
total = 0
totalChange = 0 
dateChange = []
mo2mo = {}


budget_csv = os.path.join("/Users/joshuafeinberg/Documents/U-of-O-Bootcamp/Bootcamp_Class_Folder/Module_Challenges/Module 3 Challange/PyBank/Resources/budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        date.append(row[0])
        profloss.append(row[1])
    
#removing header rows
    date.pop(0)
    profloss.pop(0)

#printing how many months are in the data set
    dataLen = len(date)
    print ("This data set has " + str(len(date)) + " months.") 
    
#calculating total profit/loss
    for i in range(0, len(profloss)):
        profloss[i] = int(profloss[i])
        total = total + (profloss[i])
    print(f'The total profit/loss for this period is: ${total}')
#calculating the difference between months and adding it to a list
    for i in range(0, len(profloss)-1):
        difference = (profloss[i+1]) - (profloss[i])
        changes.append(difference)

    

#removing the first element in date to make a dictionary for dates: changes
    date.pop(0)
    
#creating a dictionary of months as keys and change as values, starting with the second month
    mo2mo = {date[i]: changes[i] for i in range(len(date))}
   
#calculating the average change from one month to the next
    
    for i in range(0, len(changes)):
        totalChange = totalChange + changes[i] 
    avChange = totalChange/len(changes)

    print(f'The average change from month to month for this dataset is: {round((avChange),2)}')

#getting the month with the maximum increase
    keyMax = max(mo2mo, key= lambda x: mo2mo[x])

    for key,value in mo2mo.items():
        if key == keyMax:

            print(f'The month with the greatest increase was: {key} ${value}')
    

#getting the month with the maximum decrease
    keyMin = min(mo2mo, key= lambda x: mo2mo[x])
    for key, value in mo2mo.items():
        if key == keyMin:
            print(f'The maximum decreas in profits was: {key} ${value} ')
    

    

    
    
    

    #print(f' The total profit/loss is ${total}')




    

    


