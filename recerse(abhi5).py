#reverse of number
no=int(input("Enter four digit no = "))
a=(no%10)
b=no//10
c=(b%10)
d=(a*10)+c
c=b//10
e=(c%10)
d=(d*10)+e
e=c//10
d=(d*10)+e
print("reverse of given no = ",d)




a=(d%10)+1
b=d//10
c=(b%10)+1
r=(a*10)+c
c=b//10
e=(c%10)+1
r=(r*10)+e
e=c//10+1
r=(r*10)+e

print("increament of given no = ",r)
