a={1,2,3,4,5}
b={2,4,6,8,10}
#union-|
print(a|b)
print(b.union(a)) #function
#intersection-&
print(a&b)
print(b.intersection(a)) #function
#difference
print(a-b)
print(b-a)
print(a.difference(b))
print(b.difference(a))
#symmetric difference-cannot give common elements between two sets only give unique one
print(a^b)
print(b^a)
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
