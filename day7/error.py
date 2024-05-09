#value error
while(True):
    try:
        x=int(input("enter a number:"))
        break
    except valueError as a:
        print(a)
#input output error
import sys
try:
    f=open("myfile.txt")
    s=f.readline()
    i=s.strip()  #int typecast for valueerror
    x=5/0
except IOError:
    print("I/O error")
except ValueError:
    print("could not covert to integer")
except:
    print("unexpected error")
#zero division error ,combination-try->except->else->finally
try:
    x=5/0
    print(x)
except ZeroDivisionError as a:
    print(a)
else:
    print(x)
finally:
    print("python")
