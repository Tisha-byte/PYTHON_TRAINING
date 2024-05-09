class A:
    def show(self):
        print("java")
class B(A):  # inheriting A in B class
    def put(self):
        print("hello")
class C(A):
    def get(self):
        print("python")
ob1=B()
ob2=C()
ob1.show()
ob1.put()
ob2.show()
ob2.get()