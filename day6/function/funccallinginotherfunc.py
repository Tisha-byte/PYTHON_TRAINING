def show(): #func calling in another function
    print("hello")
def put():
    print("python")
    show()
put()
def show(): #func define inside another function
    print("hello")
    def put():
     print("python")
    put()  #func calling
show()