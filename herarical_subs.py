#herarichal inheritance

class master:
    name=""
    cls=""
    scl=""
    rno=""
    s1=0
    s2=0
    s3=0
    s4=0
    s5=0
    total=0
class arts(master):
    def details(self):
        self.name=input("Enter your name : ")
        self.scl=input("Enter your school : ")
        self.cls=input("Enter your class : ")
        self.rno=input("Enter your Roll No. : ")
        self.s1=int(input("Enter marks of History = "))
        self.s2=int(input("Enter marks of Economics = "))
        self.s3=int(input("Enter marks of Geography = "))
        self.s4=int(input("Enter marks of social science = "))
        self.s5=int(input("Enter marks of drawing = "))
    def calc(self):
        self.total = self.s1 + self.s2 + self.s3 + self.s4 + self.s5
    def show(self):
        print("Name of the student is : ",self.name)
        print("School name is : ",self.scl)
        print("Class : ",self.cls)
        print("Roll no : ",self.rno)
        print("History : ",self.s1)
        print("Economics : ",self.s2)
        print("Geography : ",self.s3)
        print("Social science : ",self.s4)
        print("Drawing : ",self.s5)
        print("Total marks = ",self.total)

class science(master):
    def details(self):
        self.name=input("Enter your name : ")
        self.scl=input("Enter your school : ")
        self.cls=input("Enter your class : ")
        self.rno=input("Enter your Roll No. : ")
        self.s1=int(input("Enter marks of physics = "))
        self.s2=int(input("Enter marks of Maths = "))
        self.s3=int(input("Enter marks of chemistry = "))
        self.s4=int(input("Enter marks of computer science = "))
        self.s5=int(input("Enter marks of Biology = "))
    def calc(self):
        self.total = self.s1 + self.s2 + self.s3 + self.s4 + self.s5
    def show(self):
        print("Name of the student is : ",self.name)
        print("School name is : ",self.scl)
        print("Class : ",self.cls)
        print("Roll no : ",self.rno)
        print("Phusics : ",self.s1)
        print("Maths : ",self.s2)
        print("Chemistry : ",self.s3)
        print("Computer science : ",self.s4)
        print("Biology : ",self.s5)
        print("Total marks = ",self.total)

c1=arts()
c2=science()
c1.details()
c1.calc()
print("\n")
c1.show()
print("\n\n")
c2.details()
c2.calc()
print("\n")
c2.show()
