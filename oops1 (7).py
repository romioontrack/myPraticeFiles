# using @property to change the attribute value

class Student:
    def __init__(self,phy,chem,math):
        self.phy= phy
        self.chem = chem
        self.math = math
    
    @property
    def clapercentage(self):
        return str((self.phy+self.chem+self.math) / 3 ) + "%"
    
stud = Student(97,98,99)
print(stud.clapercentage)

stud.phy = 86
print(stud.clapercentage)