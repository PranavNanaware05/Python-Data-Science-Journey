class Employee:
    def __init__(self,id,name,salary,dep):
        self.id=id
        self.name=name
        self.salary=salary
        self.dep=dep 
        


class HR(Employee):
    def __init__(self, id, name, salary,dep,com):
        super().__init__(id, name, salary,dep)
        self.com=com

    def display(self):
        print("Employee ID    :",self.id)
        print("Emplyee name   :",self.name)
        print("Employee Salary:",self.salary)
        print("Department     :",self.dep)
        print("Commission     :",self.com) 
        print("=============================")     


            
class Manager(Employee):
   def __init__(self, id, name, salary, dep,all):
       super().__init__(id, name, salary, dep,)
       self.all=all

   def display(self):
            print("Employee ID    :",self.id)
            print("Emplyee name   :",self.name)
            print("Employee Salary:",self.salary)
            print("Department     :",self.dep)
            print("Allowance      :",self.all) 
            print("=============================")     


h1=HR(101,"Pranav",10000,"HR",1000)      
h1.display()

m1=Manager(103,"Rahul",20000,"Manager",2000)
m1.display()