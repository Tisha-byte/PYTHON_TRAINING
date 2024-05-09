class A:
    def show(self):
        print("java")


class B(A):      #inheriting A in B class
    def put(self):
        ob=A()    #has a relationship
        ob.show()
        print("hello")
ob=B()
ob.show()     #is a relationship
ob.put()

