def fun(s):
    return s.upper()
str=input("enter  a string:")
u_list=map(fun,str)
for i in u_list:
    print(i,end="")