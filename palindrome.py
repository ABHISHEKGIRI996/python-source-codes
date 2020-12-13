#palindrom
no=input("ENTER ANY INTEGER : ")
ln=len(no)
no1=int(no)

print("FOR LOOP")
r=0
for i in range (0,ln):
    a=no1%10
    no1=no1//10
    if(a==0):
        r=r*10+no1
    else:
        r=r*10+a

if(r==int(no)):
    print("GIVEN NUMBER IS PALINDROME !!!!! ",r)
else:
    print("NUMBER IS NOT PALINDROME ",r)



print("\n")
print("WHILE LOOP")
re=0
j=ln-1
while j>=0:
    re=re*10+int(no[j])
    j=j-1

if(re==int(no)):
    print("GIVEN NUMBER IS PALINDROME !!!!! ",re)
else:
    print("NUMBER IS NOT PALINDROME ",re)
