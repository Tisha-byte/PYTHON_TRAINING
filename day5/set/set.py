'''set=unordered collection,cannot contain duplicate(unique) value,can perform union,intersection
symmetric diffrence,does not have key value pair,can have mixed value etc
set={}'''
set={1,(1,2,3),"tisha"}
print(set)
#add func,update=for adding data
#add func=add 1 data only
#update=can add list(it will print elements of list separately),tuple,set
set.add(7)
print(set)
set.update([8,9,0])
print(set)
#discard,remove-removing elements from sets
set.discard(1)
print(set)
set.remove("tisha")
print(set)