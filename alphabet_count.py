#alphabet count


st=input("Enter any sentence ")
print(st.upper())
st=st.lower()
l=len(st)
count=0
c=0
for i in range(0,l):
    if st[i]==" ":
        c=c+1

print("Number of words used = ",c+1)

print("\n Number of small letters use \n")
for i in range(97,123):
    for j in range(0,l):
       if st[j]==chr(i):
           count=count+1
    print(chr(i)+" = ",count)
    count=0
    
"""print("\n Number of upper letters use \n")
for i in range(65,91):
    for j in range(0,l):
       if st[j]==chr(i):
           count=count+1
    print(chr(i)+" = ",count)
    count=0"""
