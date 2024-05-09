import pymysql as sql
c=sql.connect(host="localhost",user="root",password="password",database="gits_demo")
con=c.cursor()
def InsertRecord():
    id=int(input("enter ID: "))
    n=input("enter name: ")
    p=input("enter password: ")
    city=input("enter city: ")
    q="insert into login values('%d','%s','%s','%s')"%(id,n,p,city)
    r=con.execute(q)
    if(r>0):
        print("Record Insert")
    else:
        print("Record Not insert")
    c.commit()
InsertRecord()