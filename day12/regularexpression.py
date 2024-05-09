#regular expression=> use to find pattern of string
#searches,finding,break,replace any string
#match->valye string k starting m h
#find->agr value mil gyi
import re
x=(re.match(r'Hello',"Hello Java and Python"))
print(x.group(0))
x=(re.search(r'Hello',"Java Hello and Python Hello"))
print(x.group(0))
x=(re.findall(r'Hello',"Java Hello and Python Hello"))
print(x)