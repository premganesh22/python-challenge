import csv
filepath = "C:/Users/pe415247/Desktop/Assignment2/PREWORK_PE/python-challenge/PyPoll/election_data.csv"

f = open("PyPoll.txt","w")

candidate = {}

#Reading the content in Excel and store it in a list
with open(filepath,"r") as fileObj:
    election_data = csv.reader(fileObj)
    csv_header = next(election_data)
    
    dataset = [data for data in election_data]
        

#Storing all the candidates and there votes in Dictionary 
for i in range(len(dataset)):
    if not dataset[i][2] in candidate:
        candidate[dataset[i][2]] = 1
    else:
        candidate[dataset[i][2]]+=1


print("Election Results")
f.write("Election Results\n")
print("---------------------------\n")
f.write("---------------------------\n")

#The total number of votes cast
print(f"Total Votest: {len(dataset)}")
f.write(f"Total Votest: {len(dataset)}\n")
print("---------------------------")

#A complete list of candidates who received votes
for k,v in candidate.items():
    print(f"{k}: {'{0:.2f}'.format((v/len(dataset))*100)}% ({v})")
    f.write(f"{k}: {'{0:.2f}'.format((v/len(dataset))*100)}% ({v})\n")
print("---------------------------")
f.write("---------------------------\n")

#The winner of the election based on popular vote.
winner = {v:k for k,v in candidate.items()}
print(f"Winner: {winner[max(winner)]}")
f.write(f"Winner: {winner[max(winner)]}\n")
print("---------------------------")
f.write("---------------------------\n")

#Closing notepad and CSV file
f.close()
fileObj.close()
