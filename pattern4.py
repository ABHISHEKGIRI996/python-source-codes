#pattern triangle 180 degree downside

n=int(input("enter row number : "))
l=n
for i in range (0,n):
    for j in range(0,i+1):
        print(end="  ")
    for k in range(l,0,-1):
        print("*",end=" ")
    l=l-1
    print()
