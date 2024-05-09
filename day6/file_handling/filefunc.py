#open func-it has two arguments 1st name of file and 2nd mode of file
#to create file we use this mode=> w,w+,a
'''paths=>1)relative path=>only file name is use.it is used when file and code is executed in same location.
it is written string format'''
# 2) absolute path=>if location is also mention
#forward slash=>double
#backward slash=>single
#slash in path=>file separater

x=open("gits.txt","r")
#to write in file
z=x.read()
print(z)
t=open("tisha.txt","w")
import shutil
shutil.copyfile("gits.txt","tisha.txt")
import os
os.rename("gits.txt","t2.txt")
os.remove("tisha.txt")

