#constructor->init keyword
#destructor->del keyword
class A:
    def __init__(self):     #constructor
        print("hello")
    def __del__(self):      #destructor
        print("java")
ob=A()     #object intialization