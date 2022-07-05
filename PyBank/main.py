"""
#PyBank Instructions
In this challenge, we are tasked with creating a Python script to analyze the financial records of our company. 
We need to give a set of financial data called budget_data.csv.
The dataset is composed of two columns: "Date" and "Profit/Losses". 
The task is to create a Python script that analyzes the records to calculate each of the following:
1)The total number of months included in the dataset
2)The net total amount of "Profit/Losses" over the entire period
3)The changes in "Profit/Losses" over the entire period, and then the average of those changes
4)The greatest increase in profits (date and amount) over the entire period
5)The greatest decrease in profits (date and amount) over the entire period
"""

#Import csv and os module
import os
import csv


#source to read budget data file
fileLoadPyBank = os.path.join("Resources","budget_data.csv")
#To check if we are in the correct folder and filepath, print fileLoad
#print(fileLoad)

#file to hold the output of the budget_data analysis
OutputFile = os.path.join("Analysis", "BudgetDataAnalysis.txt")

#Declare variables
TotalMonths = 0 # initial accumulator to 0
NetProfit_Loss = 0 #initialize the net total profit/losses to 0 
MonthlyChanges = [] #initialize the list of monthly changes 
Months = []   #intializes the list of months for the greatest increase and decrease


#read the csv file 
with open(fileLoadPyBank) as budget_data:
    # create a csv reader object
    csvreader = csv.reader(budget_data) #read the budget data

    #read the header row 
    header = next(csvreader) 

    #move to the first row inorder to get the previous value of profit/loss
    FirstRow = next(csvreader) # next is used again to move down to the first value of the data (of profit/loss)

    #increment the count of total months
    TotalMonths += 1 
 
    #add to the net total amount of profit/losses
         # profit/losses is in index 1
    NetProfit_Loss += int(FirstRow[1])
    #establish the previous profit/loss
        # profit/losses is in index 1
    previousProfit_loss = float(FirstRow[1]) #grabbing the first value in the row and index 1




   
    for row in csvreader:
        #increment the count of total months
        TotalMonths += 1 

        #add to the net total amount of profit/losses
        # profit/losses is in index 1
        NetProfit_Loss += int(row[1])

        #calculate the net change of profit/losses in all months
        netChange = float(row[1]) - previousProfit_loss
        #add on to the list of monthly changes
        MonthlyChanges.append(netChange)

        #add the first month where the change occured
        #month is in index 0
        Months.append(row[0])



        #update the previous profit/loss value
        previousProfit_loss = float(row[1])

#Calculate the average net change per month
AverageNetChange = sum(MonthlyChanges) / len(MonthlyChanges)


GreatestIncrease = [Months[0], MonthlyChanges[0]] # holds the month and the value of the greatest increase
GreatestDecrease = [Months[0], MonthlyChanges[0]]# holds the month and the value of the greatest decrease

#use this loop to calculate the index of the greatest and least monthly change 

for m in range (len(MonthlyChanges)):
    #calculate the greatest increase and decrease
    if (MonthlyChanges[m] > GreatestIncrease [1]):
        #if the value is greater than the greatest increase, then the value becomes the new greatest increase
        GreatestIncrease[1] = int(MonthlyChanges[m])
        #update the month
        GreatestIncrease[0] = Months[m]
    
    if(MonthlyChanges[m] < GreatestDecrease [1]):
        #if the value is greater than the greatest decrease, then the value becomes the new greatest decrease
        GreatestDecrease[1] = int(MonthlyChanges[m])
        #update the month
        GreatestDecrease[0] = Months[m]



#start generating the output in the terminal/gitbash
Output = (
        
        f"Financial Analysis \n"
        f"-----------------------------------\n"
        f"Total Months : {TotalMonths}\n"
        f"Total : ${NetProfit_Loss}\n"
        f"Average Change : $ {AverageNetChange:.2f}\n"
        f"Greatest Increase in Profits : {GreatestIncrease[0]} (${GreatestIncrease[1]})\n"
         f"Greatest Decrease in Profits : {GreatestDecrease[0]} (${GreatestDecrease[1]})\n"

        )

#print the output in the terminal/gitbash
print(Output)


 #start generating/export the output in the output text file i.e the BudgetDataAnalysis text file 
with open(OutputFile, "w") as textfile:
    textfile.write(Output)



