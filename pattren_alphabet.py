#pattern for alphabet


n=int(input("enter your number : "))

for i in range(65,65+n):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()

print("\n\n")

for i in range(65,65+n):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print()

print("\n\n")

num=65
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(num),end=" ")
        num=num+1
    print()



