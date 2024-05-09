x=int(input("enter a number:"))
m=x
sum=0
rem=0
while(x!=0):
    rem=x%10
    sum=(rem*rem*rem)+sum
    x=x//10
print(sum)
if(m==sum):
    print("number is armstrong")
else:
    print("number is not armstrong")