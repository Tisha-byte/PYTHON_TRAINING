keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
z=zip(keys,values)
dict1=dict(z)
print(dict1)
res = {}
for key in keys:
    for value in values:
        res[key] = value
        values.remove(value)
        break
print(res)