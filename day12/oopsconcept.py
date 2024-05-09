class A(object):
    pass              #classA->subclass,object_>superclass
class B:
    x=5
    def show(self):
        print("Hello")
#create a object of class
ob = B()          #object intialization
print(ob.x)
ob.show()
