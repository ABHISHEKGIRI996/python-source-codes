#luck draw
l=20
print("\n _-_-_-_- LUCKY DRAW -_-_-_-_")
no=int(input("ENTER YOUR LUCKY NUMBER : "))
if(no==l):
    print("\n YOU WON THE LUCKY DRAW !!!!!!!!!!!")
elif(no>l):
    print("\n BETTER LUCK NEXT TIME ")
    print("YOUR NUMBER IS GREATER THAN LUCKY DRAW NUMBER ")
else:
    print("\n BETTER LUCK NEXT TIME ")
    print("YOUR NUMBER IS SMALLER THAN LUCKY DRAW NUMBER ")

