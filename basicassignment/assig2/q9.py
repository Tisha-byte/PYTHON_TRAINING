days=int(input("enter the number of days:"))
years = int(days/365)
weeks = int((days % 365) / 7)
days = int(days - ((years * 365) + (weeks * 7)))
print("years:",years)
print("weeks:",weeks)
print("days:",days)
