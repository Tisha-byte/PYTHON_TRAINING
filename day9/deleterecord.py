import pymysql as sql
c=sql.connect(host="localhost",user="root",password="password",database="gits_demo")
con=c.cursor()
def DeleteRecord():
    id=int(input("enter ID:  "))
    q="delete from login where id='%s'"%(id)
    r = con.execute(q)
    if (r > 0):
        print("Record Delete")
    else:
        print("Record Not Delete")
    c.commit()
DeleteRecord()
