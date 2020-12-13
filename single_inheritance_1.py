#single inherritance 1

class parent:
    parent_name=" "
    child_name=" "
    def dis_parent(self):
        print(self.parent_name)

class child(parent):
    def dis_child(self):
        print(self.child_name)


ch1=child()
ch1.parent_name="Abhishek"
ch1.child_name="Gary"
ch1.dis_parent()
ch1.dis_child()
