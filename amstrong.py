#armstrong number
print("ARMSTRONG NUMBER IN b/W 1 To 1000")

for i in range(0,1000):

    if (i>=0 and i<=9):
        a=i
        if (a==i):
            print(i,a)
        else:
            print(" ")
    if (i>=10 and i<=99):
        a=i%10
        b=i//10
        c=(a*a) + (b*b)
        if (c==i):
            print(i,c)
            
    if (i>=100 and i<=999):
        a=i%10
        b=i//10
        c=b%10
        d=b//10
        f=(a*a*a) + (c*c*c) + (d*d*d)
        if (f==i):
            print(i,f)
