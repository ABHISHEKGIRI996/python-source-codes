#prime number
def prime(a):
    r=1
    for i in range(2,a):
        if a%i==0:
            r=0
    return r
no=int(input("Enter any integer : "))
f=prime(no)
if (f==0):
    print("Not a primt number !!!!!")
else:
    print("This number is a prime number !!!!!!!")
    
       
