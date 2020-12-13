#sum of digit
no=input("ENTER ANY INTEGER : ")
ln=len(no)
no1=int(no)

s=0
for i in range (0,ln):
    a=no1%10
    no1=no1//10
    if(a==0):
        s=s+no1
    else:
        s=s+a

print("sum of digit : ",s)



print("\n")
add=0
for j in range(0,ln):
    add=add+int(no[j])
print("sum of digit : ",add)


