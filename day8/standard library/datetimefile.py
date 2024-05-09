#DATE TIME MODULE
import datetime


print(datetime.datetime(2023,10,22)) #yyyy-mm-dd-hr-min-sec
x=datetime.datetime.today()
y=datetime.datetime(2003,10,22)
print(x-y)
import calendar
print(calendar.month(2003,10))
for i in range(1,13):       #printting all the months of year
   print(calendar.month(2003,i))
print(datetime.date.today().strftime("%y"))  #current year
print(datetime.date.today().strftime("%w"))   #week day
print(datetime.date.today().strftime("%W"))   #week number of year
print(datetime.date.today().strftime("%j"))    #day of year
print(datetime.date.today().strftime("%d"))  #day of month
print(datetime.date.today().strftime("%A")) #day of week