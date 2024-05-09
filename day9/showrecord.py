import pymysql as sql
c=sql.connect(host="localhost",user="root",password="password",database="gits_demo")
con=c.cursor()
def show():
    qur="select *from login"
    con.execute(qur)
    for data in con.fetchall():
        print(data[0]," ",data[1]," ",data[2]," ",data[3],"\n")
show()