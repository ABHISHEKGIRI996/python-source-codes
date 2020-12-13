#text file
#E:\abhipy.txt

file=open("E:/abhipy.txt",'r')
con=file.read()
print(con)
file.close()

print()

file=open("E:/abhipy.txt",'w')
a=input("WRITE ANYTHING ")
file.write(a)
file.close()


print()

file=open("E:/abhipy.txt",'r')
con=file.read()
print(con)
file.close()



b=input("enter path and file name (E:/file name.txt): ")
b="E:/"+b+".txt"
file=open(b,'w')
n=input("WRITE SOMETHING NEW ")
file.write(n)
file.close()

print()

file=open(b,'r')
con=file.read()
print(con)
file.close()


file=open(b,'a')
no=input("write a new line : ")
file.write(no)
file.close()

print()

file=open(b,'r')
con=file.read()
print(con)
file.close()


