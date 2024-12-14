#change the class attibutss

class Student:
    def __init__(self,phy,chem,math):
        self.phy= phy
        self.chem = chem
        self.math = math
        
    def percentage(self):
        per = str((self.phy+self.chem+ self.math)/3) + "%"
        print(per)
        
stud = Student(97,98,99)
print(stud.percentage())

stud.phy =86
print(stud.percentage())

    
        