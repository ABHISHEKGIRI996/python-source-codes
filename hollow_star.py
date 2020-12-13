#hollow triangle


n=int(input("enter your number ; "))

l=1

for i in range (n,0,-1):
    for j in range (0,i):
        print(end=" ")

    for k in range (0,l):
        if (k==0):
            print("*",end=" ")
        if(k>0):
            if (k==l-1):
                print(end="*")
        if (k>0) and (k<l-1) :
            print(end="  ")
    l+=1
    print()


l=n
for i in range (1,n):
    for j in range (0,i+1):
        print(end=" ")
    for k in range (1,l):
        if(k>1): 
            if (k==l-1):
                print(end="*")

        if (k==1):
            print(end="*")
        
        if (k>0) and (k<l-1) :
            print(end="  ")
    l=l-1
    print()
    
