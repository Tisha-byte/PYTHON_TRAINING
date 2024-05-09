'''dictionary-unordered collection,mutable,cannot perform indexing,slicing and steping,add data in pair ie
 key value pair,key should unique but value may be same and duplicate,key can hold list,tuple,dictionary'''
x={1:"java",2:"html",3:"python"}
print(x)
x={1:"java",1:"html",2:"python"}
print(x)
#accesing data by key
print(x[2])
#accesing keys
print(x.keys())
#accesing values
print(x.values())
print(x.get(2,1))
x={'a':"hello",'b':"java"}
x['l']=list(range(5))
x['t']=tuple(sorted(range(9,16),reverse=True))
print(x.keys())
print(x.values())
for k,v in x.items():
    print(k," : ",v)
