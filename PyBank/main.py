import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")


date = []
daily_pl = []

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
        date.append(row[0])
        daily_pl.append(row[1])


date_count = len(date)


total = 0

for x in range(len(daily_pl)):
    total = int(daily_pl[x]) + total


change_pl = []

for i in range(len(daily_pl)):
    change = int(daily_pl[i]) - int(daily_pl[i-1])
    change_pl.append(change)

change_total = 0

for y in range(1,len(daily_pl)):
    change_total = int(change_pl[y]) + change_total

average_change_pl = change_total / (len(change_pl)-1) 

max_change = max(change_pl)
min_change = min(change_pl)

max_date = date[change_pl.index(max_change)]
min_date = date[change_pl.index(min_change)]

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {date_count}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change_pl}')
print(f'Greatest Increase in Profits: {max_date} (${max_change})')
print(f'Greatest Decrease in Profits: {min_date} (${min_change})')


output_file = os.path.join("pybank.txt")

with open(output_file, "w",) as textfile:
    print("Financial Analysis", file=textfile)
    print("----------------------------", file=textfile)
    print(f'Total Months: {date_count}', file=textfile)
    print(f'Total: ${total}', file=textfile)
    print(f'Average Change: ${average_change_pl}', file=textfile)
    print(f'Greatest Increase in Profits: {max_date} (${max_change})', file=textfile)
    print(f'Greatest Decrease in Profits: {min_date} (${min_change})', file=textfile)