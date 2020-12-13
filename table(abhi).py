#table

a=int(input("enter your range (first number): "))
b=int(input("enter your range (second number): "))

no=int(input("enter any integer : "))
i=1
while i<=10:
   print(no,"*",i,"=",no*i)
   i=i+1

print("\n")




for j in range(a,b+1):
    print("-----------------")
    for k in range (1,11):
        print(j,"*",k,"=",k*j)
    

    

#print("enter your range : ")
