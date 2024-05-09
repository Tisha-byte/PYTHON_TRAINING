employees = ['Ram', 'Amit']
defaults = {"designation": 'Developer', "salary": 8000}
k=list(defaults.items())
print(k)
dict1=d
z=zip(employees,defaults)
dict1=dict(z)
print(dict1)
