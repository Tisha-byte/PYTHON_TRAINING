def fun(lis1,lis2):
    return lis1+lis2
x=[1,2,3,4,5,6]
y=[12,34,56,78,90,2]
u_list=map(fun,x,y)
print(list(u_list))
