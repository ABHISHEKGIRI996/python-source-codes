#guessing number
import random
print("Think a number in your between 1 to 10 and keep the number in your mind")
input("press Enter for next instruction ")
print()
print("take same number from your friend and add both number ")
input("press Enter for next instruction \n")
r = random.choice([2,4,6,8,10])
print("add this number to your resultant number ",r)
input("press Enter for next instruction \n")
print("Divide your number by 2 ")
input("press Enter for next instruction \n")
print("give back the number that you have taken from your friend ")
input("press enter for finals\n")
f=r//2

print("Right now you have : ",f)
