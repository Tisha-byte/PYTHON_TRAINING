import csv
with open("pqr.csv","r",encoding="UTF8",newline="") as f:
    w1=csv.reader(f)
    for i in w1:
        print(i)