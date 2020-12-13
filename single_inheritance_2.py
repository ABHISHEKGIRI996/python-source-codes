#addition with heritance
class add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("first no      = ",self.a)
        print("second no     = ",self.b)
        print("sum of two no = ",self.c)

class sum1(add):
    def calc(self):
        self.c=self.a+self.b
        print("Addition of two number : ",self .c)
n=int(input("enter first integer : "))
k=int(input("enter your second integer : "))
s1=sum1(n,k)
s1.calc()
s1.display()

    
        
