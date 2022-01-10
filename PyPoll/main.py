import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# declare a bunch of variables for later
total_votes = 0
candidates_unique = []

khan_votes = 0
correy_votes = 0
li_votes = 0
tooley_votes = 0

# open the csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)

# loop through the rows
    for row in csvreader:

# tally the total votes 
        total_votes += 1

# Find the unique candidates and add them to a list
        if row[2] not in candidates_unique:
            candidates_unique.append(row[2])

# Talley votes for each candidate        
        if row[2] == "Khan":
            khan_votes += 1
        
        elif row[2] == "Correy":
            correy_votes += 1
        
        elif row[2] == "Li":
            li_votes += 1

        elif row[2] == "O'Tooley":
            tooley_votes += 1

# calculate rounded percentages

khan_percentage = round(khan_votes / total_votes * 100, 3)
correy_percentage = round(correy_votes / total_votes * 100, 3)
li_percentage = round(li_votes / total_votes * 100, 3)
tooley_percentage = round(tooley_votes / total_votes * 100, 3)

# print summary

print("---------------------------------")
print("Election Results")
print("---------------------------------")
print("Total Votes: " + str(total_votes))
print("Khan: " + str(khan_percentage)+ "% — " + str(khan_votes))
print("Correy: " + str(correy_percentage)+ "% — " + str(correy_votes))
print("Li: " + str(li_percentage)+ "% — " + str(li_votes))
print("O'Tooley: " + str(tooley_percentage)+ "% — " + str(tooley_votes))
print("---------------------------------")
print("Winner: Khaaaaaaan!")
print("---------------------------------")
