#largets number
def large(a,b,c):
    m=a
    if (m<b):
       m=b
    if (m<c):
       m=c

    print("largest no is = ",m)


a=int(input("ENTER YOUR FIRST NUMBER  = "))
b=int(input("ENTER YOUR SECOND NUMBER = "))
c=int(input("ENTER YOUR THIRD NUMBER  = "))
large(a,b,c)



