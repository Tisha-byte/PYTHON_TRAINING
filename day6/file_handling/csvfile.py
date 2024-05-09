import csv
data=[]
name=input("enter name:")
data.append(name)
age=int(input("enter age:"))
data.append(age)
city=input("enter city:")
data.append(city)
salary=int(input("enter salary:"))
data.append(salary)
with open("pqr.csv","a",encoding="UTF8",newline="") as f:
    w1=csv.writer(f)
    w1.writerow(data)
