


n=int(input("Enter your row number : "))

l=n


for i in range (0,n):
    for j in range (0,l):
        print(end=" ")
    l=l-1
    for k in range (0,i+1):
        print("*",end=" ")
    print()
l=n
for i in range(1,n):
    for j in range(0,i+1):
        print(end=" ")
    for k in range(1,l):
        print("*",end=" ")
    l=l-1
    print()

