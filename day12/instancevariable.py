#instance variable ->variable which is passed in function as parameter.
# Instance variable's value changes
#class variable->variable which is defined in class.
# class variabkle value always remain same with object
class A:
    city="Udaipur"       #class variable
    def show(self,name,age):       #instance variable
        print(name,age)
ob=A()
print(ob.city)
ob.show("ram",34)
print(ob.city)
ob.show("sita",24)

