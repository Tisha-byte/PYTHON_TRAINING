def put():
    print("python")
def show():
    print("python")
def get():
    print("java")
def main():
    while(True):
        print("enter your choice:\n1. show\n2. put\n3. get\n4.  exit\n")
        x=int(input("enter your choice:   "))
        if(x==1):
            show()
        elif(x==2):
            put()
        elif(x==3):
            get()
        else:
            break
main()