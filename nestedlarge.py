#largest of three number using nested ifelse
a=int(input("enter your first number  = "))
b=int(input("enter your second number = "))
c=int(input("entr your third number   = "))
if(a>b):
    if(a>c):
        print("\n Largest number is : ",a)
    else:
        print("\n Largest number is : ",c)

else:
    if(b>a):
        if(b>c):
            print("\n Largest number is : ",b)
        else:
            print("\n Largest number is : ",c)




        
