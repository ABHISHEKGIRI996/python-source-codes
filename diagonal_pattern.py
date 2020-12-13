#diagonal represion
a=int(input("Enter row number "))

for i in range(1,a+1):
    for j in range(1,a+1):
        if ((i==j) or i+j==a+1 ):
            print(end="*")
        else:
            print(end=" ")
    print()
