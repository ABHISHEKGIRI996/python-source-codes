#multiple inheritance 2

class radi:
    radius=0
    area=0
    def __init__(self,r):
        self.radius=r
    def rad(self):
        print("radius of circle : ",self.radius)
class pie:
    pi=3.14
    def piee(self):
        print("Value of pie is : ",self.pi)

class area(radi,pie):
    def calc(self):
        self.ar=self.pi*(self.radius*self.radius)
    def show(self):
        print("radius of circle ",self.radius)
        print("value of pie ",self.pi)
        print("Area of circle is ",self.ar)
rs=int(input("enter the rardius of circle : "))
r1=area(rs)
r1.calc()
r1.rad()
r1.piee()
r1.show()
