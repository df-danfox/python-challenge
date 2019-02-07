#import modules
import os
import csv


#set file path
csvpath = os.path.join('..','budget_data.csv')
 

#read csv file 
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')


    # Ignore the header row
    header = next(csvreader)

    #define list from the columns in csvfile
    dates = []
    pandl = []
    plchange = []
    
    #append values to column
    for x in csvreader:
        dates.append(x[0])
        pandl.append(int(x[1]))     
    for y in range(len(pandl)-1):
        plchange.append(pandl[y+1]-pandl[y])   

       
    #check output        
    #print(csvpath)
    #print(dates)
    #print('------')
    #print(pandl)
    #print('------')
    #print (plchange)


#The total number of months included in the dataset
TotalMonth=len(dates)

#The net total amount of "Profit/Losses" over the entire period
NetTotalPl=sum(pandl)

#The average of the changes in "Profit/Losses" over the entire period
Average_Change=round(sum(plchange)/len(plchange),2)

#The greatest increase in profits (date and amount) over the entire period
PIncrease= max(plchange)
#create value from index -Increase in Profits for month
MIncrease = plchange.index(max(plchange))+1

#The greatest decrease in losses (date and amount) over the entire period
PDecrease=min(plchange)
#create value from index - Decrease in Profits for month
MDecrease = plchange.index(min(plchange))+1

#Send results to screen
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(dates)}")
print(f"Total: ${sum(pandl)}")
print(f"Average Change: ${round(sum(plchange)/len(plchange),2)}")
print(f"Greatest Increase in Profits: {dates[MIncrease]} (${(str(PIncrease))})")
print(f"Greatest Decrease in Profits: {dates[MDecrease]} (${(str(PDecrease))})")      

#Send results to txt file called Output.txt
with open("Output.txt", "w") as text_file:
    print(("Financial Analysis"), file=text_file)
    print(("------------------------"), file=text_file)
    print((f"Total Months: {len(dates)}"), file=text_file)
    print((f"Total: ${sum(pandl)}"), file=text_file)
    print((f"Average Change: ${round(sum(plchange)/len(plchange),2)}"), file=text_file)
    print((f"Greatest Increase in Profits: {dates[MIncrease]} (${(str(PIncrease))})"), file=text_file)
    print((f"Greatest Decrease in Profits: {dates[MDecrease]} (${(str(PDecrease))})"), file=text_file)  