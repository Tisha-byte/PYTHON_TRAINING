bs=float(input("enter the salary:"))
if(bs<=10000):
    gs=bs+bs*0.2+bs*0.8
    print(gs)
elif(bs<=20000):
    gs = bs + bs * 0.25 + bs * 0.9
    print(gs)
else:
    gs=bs+bs*0.3+bs*0.95
    print(gs)