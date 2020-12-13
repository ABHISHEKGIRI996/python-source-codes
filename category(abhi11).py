#ticket category
age=int(input("Enter your age : "))

if(age<=3):
    print("Your ticket price is FREE")
elif(age>=4 and age<=10):
    print("Your ticket price is 100/-")
elif(age>=11 and age<=20):
    print("Your ticket price is 200/-")
elif(age>=21 and age<=30):
    print("Your ticket price is 300/-")
elif(age>=31 and age<=40):
    print("Your ticket price is 400/-")
else:
    print("Your ticket price is 500/-")

