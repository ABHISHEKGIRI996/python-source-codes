#fabonacci series
no=int(input("Enter your range : "))
print("\n For loop")
a=1
b=2
print(a)
print(b)
for i in range (0,no-2):
    c=a+b
    print(c)
    a=b
    b=c


print("\n while loop ")
f=1
s=2
i=0
print(f)
print(s)

while (i<no-2):
    d=f+s
    print(d)
    f=s
    s=d
    i=i+1

    
