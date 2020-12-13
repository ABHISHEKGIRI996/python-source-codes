#armstrong 2

i=int(input("ENTER ANY THREE DIGIT NO. : "))

a=i%10
b=i//10
c=b%10
d=b//10
f=(a*a*a) + (c*c*c) + (d*d*d)
if (f==i):
    print("THIS NUMBER IS A ARMSTRONG NUMBER ")
else :
    print("THIS NUMBER IS NOT A ARMSTRONG NUMBER ")


