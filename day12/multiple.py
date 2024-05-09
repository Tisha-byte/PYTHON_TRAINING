class A:
    def show(self):
        print("java")
class B:  # inheriting A in B class
    def show(self):
        print("hello")
class C(B,A):     #(A,B)->A ka func call hoga ,(B,A)_>B ka func call hoga
    def get(self):
        print("python")
#ambiguity-> it is resolve by first come first serve
ob=C()
ob.show()
ob.get()