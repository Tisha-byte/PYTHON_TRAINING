#csv=comma separated value
import csv
data=["ram",45,50000]
with open("xyz.csv","a",encoding="UTF8",newline="") as f:
    w1=csv.writer(f)
    w1.writerow(data)