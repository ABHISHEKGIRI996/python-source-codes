#report card using class

class Student:
    name=""
    cl=""
    rollno=0
    f_name=""
    mat=0
    sci=0
    sst=0
    san=0
    eng=0
    total=0
    per=0
    def __init__(self,n,c,rn,fn,mt,sc,ss,sa,en):
        self.name=n
        self.cl=c
        self.rollno=rn
        self.f_name=fn
        self.mat=mt
        self.sci=sc
        self.sst=ss
        self.san=sa
        self.eng=en
    def percentage(self):
        self.total=self.mat + self.sci + self.sst + self.san + self.eng
        self.per=self.total/5
    def show(self):
        print("Result of "+self.name)
        print("Class    : ",self.cl)
        print("Roll No. : ",self.rollno)
        print("Father name of "+self.name+" is "+self.f_name)
        print("Marks of MATHS           = ",self.mat)
        print("Marks of SCIENCE         = ",self.sci)
        print("Marks of SOCIAL SCIENCE  = ",self.sst)
        print("Marks of SANSKRIT        = ",self.san)
        print("Marks of ENGLISH         = ",self.eng)
        print("\t\t\t---------")
        print("Total marks              = ",self.total)
        print("Percentage               = ",self.per)
        if self.per >= 33 :
            print(self.name+" is PASS with",self.per,"%")
        else:
            print(self.name+"is FAIL with",self.per,"%")
        
no=int(input("How many data you want to enter : "))
for i in range(1,no+1):
    print("\n FILL THE DETAILS OF",i,"student ")
    a=input("Enter your name : ")
    b=input("Enter your class no : ")
    c=int(input("Enter your roll number : "))
    d=input("Enter your father name : ")
    print("\n FILL SUBJECT MARKS")
    s1=int(input("Enter marks of MATHS          = "))
    s2=int(input("Enter marks of SCIENCE        = "))
    s3=int(input("Enter marks of SOCIAL SCIENCE = "))
    s4=int(input("Enter marks of SANSKRIT       = "))
    s5=int(input("Enter marks of ENGLISH        = "))

    stu=Student(a,b,c,d,s1,s2,s3,s4,s5)
    stu.percentage()
    print("\n\n -------------- REPORT CARD -------------")
    stu.show()
    print("\n ------------------ END -----------------")





    
