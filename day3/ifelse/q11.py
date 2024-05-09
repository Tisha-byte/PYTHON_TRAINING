ele_bill=int(input("enter electricity bill:"))
if(ele_bill<=50):
    ele_bill=ele_bill*0.50

elif(ele_bill<=100):
    ele_bill=ele_bill*0.75

elif(ele_bill<=200):
    ele_bill=ele_bill*1.20

elif(ele_bill>=250):
    ele_bill=ele_bill*1.50


surcharge=ele_bill*0.2
ele_bill=ele_bill+surcharge
print(ele_bill)
