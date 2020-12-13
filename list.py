#list

no=[9,8,7,6,5,4,3,2,1]
print(no)
no1=["word1","word2","word3","word4","word5"]
print(no1)
no2=[1,2,3,4,"word1","word2",5,6,7,8,9,"word3","word4","word5",5,55,5,5,5,5,5,5,5,5,5]
print(no2)
print(no[6])
print(no1[3],no2[5])
print(no2[10])

print(no2[:6])
print(no2[-6:])

no2[4]=input("any value ")
print(no2)
print("\n")
no2.append(no2[4])
print(no2)

print("\n")
no.insert(4,5)
print(no)

print("\n")

no3=no+no1
print(no3)

print("\n")

print("extend + ")
no=no+no1
print(no)

print("\n")

print("extend")
no1.extend(no)
print(no)
print(no1)

print("\n")


no1.pop(4)
print(no1)

print("\n")

del no1[4]
print(no1)

print("\n")

print(no2)
no2.remove("word5")
print("\n")
print(no2)

print("\n")


if "word4" in no2:
    print("word4 present in list ")
else:
    print("word4 is not present in class ")

print("\n")

z=[3,6,23,6,7,5,4,65,76,5,9]
print(no2.count(5))
n=["a","f","n","e","n","m","u","d","v","g","e",]
print(n)
n.sort()
print("\n")
print(n)
print("\n")
z.sort()
print(z)

print("\n")


n.clear()
print(n)

print("\n")

nb=no.copy()
print(nb)








