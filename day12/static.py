#decorator_>@staticmethod
class A:
    @staticmethod
    def show():
        print("hello")
A.show()          #without object calling by class name
ob=A()
ob.show()