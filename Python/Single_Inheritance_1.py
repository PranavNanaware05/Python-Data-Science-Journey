class Employee:
    def __init__(self ,id,name,salary):
         self.id=id
         self.name=name
         self.salary=salary

class HR(Employee):
     def __init__(self,all, id, name, salary):
          super().__init__(id, name, salary)  
          self.all=all

     
     def display(self):            
        print("Employee Name:",self.name)
        print("ID           :",self.id)
        print("Salary       :",self.salary)
        print("All          :",self.all)


h1=HR(1000,101,"pranav",10000)    
h1.display()   
                