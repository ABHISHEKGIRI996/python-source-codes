#print pattern right triangle

n=int(input("Enter row of the triangle : "))

for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()




