#employee record

class Employe:
    name=""
    idno=""
    add=""
    dept=""
    att=0
    bonus=0
    ded=0
    sal=0
    tsal=0
    lev=0
    def __init__(self,n,idn,ad,dt,lv):
        self.name=n
        self.idno=idn
        self.add=ad
        self.dept=dt
        self.lev=lv
    def salary(self):
        self.att=(20-self.lev)*(100/20)

        #salary count
        if (self.dept=="manager"):
            self.sal=100000
        elif(self.dept=="group leader"):
            self.sal=75000
        elif(self.dept=="team leader"):
            self.sal=65000
        elif(self.dept=="team member"):
            self.sal=40000
        elif(self.dept=="peon"):
            self.sal=15000

        #bonus count
        if (self.att==100):
            self.bonus=(self.sal*20)/100
            self.tsal=self.sal+self.bonus
        elif(self.att>=75):
            self.bonus=(self.sal*15)/100
            self.tsal=self.sal+self.bonus
        elif(self.att>=60):
            self.bonus=(self.sal*10)/100
            self.tsal=self.sal+self.bonus
        #deduction count
        elif(self.att<60 and self.att>=50):
            self.ded=(self.sal*20)/100
            self.tsal=self.sal-self.ded
        elif(self.att<50 ):
            self.ded=(self.sal*50)/100
            self.tsal=self.sal+self.ded

    def show(self):
        print("Pay slip of "+self.name.upper())
        print("ID No                : ",self.idno)
        print("Department           : ",self.dept.upper())
        print("Address              : ",self.add)
        print("Attendence           : ",self.att,"%")
        print("Basic salary         : ",self.sal)
        print("Bonus                : ",self.bonus)
        print("Deduction            : ",self.ded)
        print("Total earned salary  : ",self.tsal)


    def __del__(self):
        print("destructor is called , all abjest has been deleted   ")




    
no=int(input("How many data you want to fill : "))
for i in range(1,no+1):
    print("FILL THE DETAILS OF",i,"EMPLOYEE")
    a=input("Enter your name        : ")
    b=input("Enter your ID number   : ")
    c=input("Enter your address     : ")
    d=input("Enter your department (manager/group leader/team leader/team member/peon) : ")
    f=int(input("Number of leave you have taken : "))


    emp=Employe(a,b,c,d,f)
    emp.salary()
    print("\n\n\n---------------- PAY SLIP ---------------")
    emp.show()
    print("\n\n------------------- END ------------------")
    del emp
    print()
