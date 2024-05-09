#function define in class is parametrized that's why python take a default parameter 'self'
# if func defination has N parameter then in calling we pass N-1 parameter
class A:
    def show(x,y):          #x->self parameter(default)
        print("hello")
        print(x)
        print(y)
ob=A()
ob.show(2)