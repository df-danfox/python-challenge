#import modules
import os
import csv

#set file path
csvpath = os.path.join('election_data.csv')

#read csv file 
with open(csvpath, newline="", encoding="utf-8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Ignore the header row
    header = next(csvreader)
    
#define list variables
    
VoterID = []
County = []
Candidate = []
CandidateName = []

with open(csvpath, "r", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    for row in csvreader:
        VoterID.append(row[0])
        Candidate.append(row[2])


#The total number of votes cast
TotalVotes = len(set(VoterID))
#TotalVotes

#A complete list of candidates who received votes
CandidateName = set(Candidate)
#CandidateName

#The total number of votes each candidate won,


# Variables 
TotalVotes = 0 
TotalCorreyVotes = 0
TotalKhanVotes = 0
TotalLiVotes = 0
TotalOTooleyVotes = 0

with open(csvpath,newline="", encoding="utf-8") as file:

    # Store data under the csvreader variable
    csvreader = csv.reader(file,delimiter=",") 

    # Skip the header so we iterate through the actual values
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        # Determine the total numvber of Total votes
        TotalVotes +=1

        # Determine how many votes are for each candidate
        if row[2] == "Correy": 
            TotalCorreyVotes +=1
        elif row[2] == "Khan":
            TotalKhanVotes +=1
        elif row[2] == "Li": 
            TotalLiVotes +=1
        elif row[2] == "O'Tooley":
            TotalOTooleyVotes +=1
#TotalVotes, TotalCorreyVotes, TotalKhanVotes, TotalLiVotes, TotalOTooleyVotes

          
# Determine Percentages
CorreyPercent = (TotalLiVotes/TotalVotes)*100
KhanPercent = (TotalKhanVotes/TotalVotes)*100
LiPercent = (TotalLiVotes/TotalVotes)*100
OTooleyPercent = (TotalOTooleyVotes/TotalVotes)*100

#CorreyPercent, KhanPercent, LiPercent, OTooleyPercent

#The winner of the election based on popular vote.

total_list = {'Correy': TotalCorreyVotes,'Khan':TotalKhanVotes ,'Li': TotalLiVotes,'OTooley': TotalOTooleyVotes}
winner = max(total_list, key=lambda key: total_list[key])
#print(winner)


# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {TotalVotes}")
print(f"----------------------------")
print(f"Khan: {KhanPercent:.3f}% ({TotalKhanVotes})")
print(f"Correy: {CorreyPercent:.3f}% ({TotalCorreyVotes})")
print(f"Li: {LiPercent:.3f}% ({TotalLiVotes})")
print(f"O'Tooley: {OTooleyPercent:.3f}% ({TotalOTooleyVotes})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")


#Send results to txt file called Election Results.txt
with open("Election Results.txt", "w") as text_file:
    print((f"Election Results"), file=text_file)
    print((f"----------------------------"), file=text_file)
    print((f"Total Votes: {TotalVotes}"), file=text_file)
    print((f"----------------------------"), file=text_file)
    print((f"Khan: {KhanPercent:.3f}% ({TotalKhanVotes})"), file=text_file)
    print((f"Correy: {CorreyPercent:.3f}% ({TotalCorreyVotes})"), file=text_file)
    print((f"Li: {LiPercent:.3f}% ({TotalLiVotes})"), file=text_file)
    print((f"O'Tooley: {OTooleyPercent:.3f}% ({TotalOTooleyVotes})"), file=text_file)
    print((f"----------------------------"), file=text_file)
    print((f"Winner:{winner} "), file=text_file)
    print((f"----------------------------"), file=text_file)
