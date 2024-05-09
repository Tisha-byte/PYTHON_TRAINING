#Abstraction=> we can achieve it by constructing abstract class
from abc import ABCMeta ,abstractmethod
class A:
    @abstractmethod
    
    def show(self):
        pass
class B(A):
    def show(self):
        print("java")

ob=B()
ob.show()