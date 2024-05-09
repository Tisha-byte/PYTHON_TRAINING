x=int(input("enter a number:"))
sum=0
rem=0
while(x!=0):
    rem=x%10
    sum=rem+sum
    x=x//10
print(sum)