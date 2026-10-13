class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class job:
    def __init__(self,id,dep):
        self.id=id
        self.dep=dep

class Details(Person,job):

     def __init__(self, name, age,id,dep):
         Person.__init__(self,name,age)
         job.__init__(self,id,dep)       

     def display(self):
        print("Name      :", self.name)
        print("Age       :", self.age)
        print("Salary    :", self.id)
        print("Department:", self.dep)


d1=Details("pranav",22,101,"IT")
d1.display()

                