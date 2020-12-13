#pattern down side triangle

n=int(input("Enter your row number : "))


l=n

for i in range (0,n):
    for j in range (0,l):
        print("*",end=" ")
    l=l-1
    print()


for k in range (n,0,-1):
   
    for j in range (0,k):
        
        print("*",end=" ")
    print()
