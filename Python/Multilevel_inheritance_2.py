class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

class HR(Employee):
    def __init__(self, id, name, salary,all):
        super().__init__(id, name, salary)
        self.all=all

class AHR(HR):
    def __init__(self, id, name, salary, all,aall):
        super().__init__(id, name, salary, all)
        self.aall=aall


    def display(self):
        print("Employee ID            :",self.id)
        print("Employee Name          :",self.name)
        print("Employee Salary        :",self.Salary)
        print("Employee Allowance     :",self.All)
        print("Employee Area Allowance:",self.aall)

a1=AHR(101,"pranav",10000,1000,500)        