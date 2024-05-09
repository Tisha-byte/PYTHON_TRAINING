#polymorphism_
#FUNCTION OVERIDDING
class A:
    def show(self):
        print("hello")
class B(A):
    def show(self):
        print("java")
ob=B()
ob.show()