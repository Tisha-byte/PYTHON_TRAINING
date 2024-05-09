class A:
    def show(self):
        print("java")
class B(A):  # inheriting A in B class
    def put(self):
        print("hello")
class C(B):
    def get(self):
        print("python")
ob=C()
ob.show()
ob.put()
ob.get()
