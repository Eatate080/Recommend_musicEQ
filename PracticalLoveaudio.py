import csv
    

n = 6
a = []
for i in range(n):
    a.append(int(input()))

with open('practice_EQdate.csv', 'a',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(a)

with open('practice_EQdate.csv', newline="") as f:
        print(f.read())