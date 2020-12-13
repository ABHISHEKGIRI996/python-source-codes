#loop in list
stu=["abhi","sumi","ravi","priya","rocky"]

print("for loop 1")
for i in stu:
    print(i)
print()
print("for loop 2")
for i in range(0,len(stu)):
    print(stu[i])

print()
print("while loop")
i=0
while i < len(stu):
    print(stu[i])
    i+=1

rollno=[[1,2,3],[4,5,6],[7,8,9]]
print(rollno[0])
print(rollno[1])
print(rollno[2])
print()
for sublist in rollno:
    for i in sublist:
        print(i)
print()

"""for i in range (0,3):
    for j in range (0,3):
        print(rollno[i][j])"""
        
no= list (range(1,21))
print(no)
print(no.index(6))
print(no.index(5,4))
