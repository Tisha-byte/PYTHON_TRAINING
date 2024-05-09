import pymysql as sql
c=sql.connect(host="localhost",user="root",password="password",database="gits_demo")
con=c.cursor()
def UpdateRecord():
    id=int(input("enter ID: "))
    p=input("enter password: ")
    city=input("enter city: ")
    q="update login set password='%s',city='%s'where id='%d'"%(p,city,id)
    r=con.execute(q)
    if (r > 0):
        print("Record Update")
    else:
        print("Record Not Update")
    c.commit()
UpdateRecord()
