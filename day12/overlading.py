#python does not support function overloading
class A:
    def show(self):
        print("hello")
    def show(self,x):
        print("java")
    def show(self,x,y):
        print("python")
ob=A()
#ob.show()
#ob.show(1)
ob.show(1,2)

# function overloading achieving by default paramter
class B:
    def show(self,a=None,b=None,c=None):
        if(a!=None and b==None or c==None):
            print("hello")
        else:
            print("python")
ob1=B()
ob1.show()
