#fabonacci with function
def fab(r):
    a=1
    b=2
    print(a)
    print(b)
    for i in range (0,r-2):
        c=a+b
        print(c)
        a=b
        b=c

no=int(input("ENTER YOUR RANGE : "))
fab(no)
