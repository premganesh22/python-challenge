import csv
filepath = "C:/Users/pe415247/Desktop/Assignment2/PREWORK_PE/python-challenge/PyBank/budget_data.csv"

f = open("PyBank.txt","w")

# Declaring all the requirement Variable
total_months = 0
net_profit = 0
dataset = []
average = []
profit_increase = float("-inf")
profit_decrease = float("inf")

#Reading the CSV and store the data in list
with open(filepath,"r") as fileObj:
    budget_data = csv.reader(fileObj)
    csv_header = next(budget_data)
    
    dataset = [data for data in budget_data]
        
# Loop through all the data in list
for i in range(len(dataset)):
    #The total number of months included in the dataset
    total_months+=1
    net_profit+=int(dataset[i][1])
    
    if not i ==  len(dataset)-1:
        difference = float(dataset[i+1][1]) - float(dataset[i][1])
        average.append(difference)
        if profit_increase < difference:
            profit_increase = difference
            profit_inc_month = dataset[i+1][0]

        if profit_decrease > difference:
            profit_decrease = difference
            profit_dec_month = dataset[i+1][0]

average_change = "{0:.2f}".format((sum(average)/len(average)))

        
#The total number of months included in the dataset
print(f"Total Months: {total_months}")
f.write(f"Total Months: {total_months}\n")

#The total net amount of "Profit/Losses" over the entire period

print(f"Total: ${net_profit}")
f.write(f"Total: ${net_profit}\n")

#The average change in "Profit/Losses" between months over the entire period
print(f"Average Change: ${average_change}")
f.write(f"Average Change: ${average_change}\n")

#The greatest increase in profits (date and amount) over the entire period
print(f"Greatest Increase in Profits: {profit_inc_month} (${int(profit_increase)})")
f.write(f"Greatest Increase in Profits: {profit_inc_month} (${int(profit_increase)})\n")

#The greatest decrease in losses (date and amount) over the entire period
print(f"Greatest Decrease in Profits: {profit_dec_month} (${int(profit_decrease)})")
f.write(f"Greatest Decrease in Profits: {profit_dec_month} (${int(profit_decrease)})\n")

f.close()
fileObj.close()
