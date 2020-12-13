#multiple inheritance 1

class father:
    f_name=" "
    def show_father(self):
        print(self.f_name)
class mother:
    m_name=" "
    def show_mother(self):
        print(self.m_name)
class son(father,mother):
    def show(self):
        self.show_father()
        self.show_mother()
        print("father name : ",self.f_name)
        print("mother name : ",self.m_name)


s1=son()
s1.f_name="Rahul Jha "
s1.m_name="Simran Jha"
s1.show()
    
