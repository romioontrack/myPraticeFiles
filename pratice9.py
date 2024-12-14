#define class Employee with attributes role, Department & salary.
# Define the method show
# By using ineritance property of class use the attibutes Employee

class Employe:
    def __init__(self,role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
        
    def show(self):
        print("Role of Employee is :",self.role)
        print("The department of employee is :",self.department)
        print("The salary of employee is :", self.salary)
        
class Engineer(Employe):
    def __init__(self, name, age):
        self.name =name
        self.age = age  
        super().__init__ ("Engineer", "IT", "75000")      # class Inheritance works
        
e1 = Engineer("RamJEE", 23 )
e1.show()