import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")


voter_id = []
county = []
vote = []

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        vote.append(row[2])


total_votes = len(vote)


unique_candidates = list(set(vote))


count_num=[]
count_pct=[]

for candidate in range(len(unique_candidates)):
    count_num.append(0)
    count_pct.append(0)

for candidate in range(len(unique_candidates)):
    count_num[candidate] = vote.count(unique_candidates[candidate])

for x in range(len(count_num)):
    count_pct[x] = count_num[x] / total_votes


count_sort = sorted(count_num, reverse=True)

sort_key = []

for y in range(len(count_sort)):
    key_num = count_num.index(count_sort[y])
    sort_key.append(key_num)


print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
for z in range(len(unique_candidates)):
    print(f'{unique_candidates[sort_key[z]]}: {str(round(count_pct[sort_key[z]]*100,3))}% ({count_num[sort_key[z]]})')
print("-------------------------")
print(f'Winner: {unique_candidates[sort_key[0]]}')
print("-------------------------")


output_file = os.path.join("pypoll.txt")

with open(output_file, "w",) as textfile:
    print("Election Results", file=textfile)
    print("-------------------------", file=textfile)
    print(f'Total Votes: {total_votes}', file=textfile)
    print("-------------------------", file=textfile)
    for z in range(len(unique_candidates)):
        print(f'{unique_candidates[sort_key[z]]}: {str(round(count_pct[sort_key[z]]*100,3))}% ({count_num[sort_key[z]]})', file=textfile)
    print("-------------------------", file=textfile)
    print(f'Winner: {unique_candidates[sort_key[0]]}', file=textfile)
    print("-------------------------", file=textfile)