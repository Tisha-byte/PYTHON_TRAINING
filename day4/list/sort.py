#ascendung order sort
x=[75,98,45,67,78,90]
x.sort()
print(x)
#descending order sort
x.sort(reverse=True)
print(x)
#sorted
print(sorted(x))
print(sorted(x,reverse=True))
#sorting in string
x=["Ram","Amit","A"]
#sorting on the based of string length
x.sort(key=len)
print(x)