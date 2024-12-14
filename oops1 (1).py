class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks= marks
    
    def average(self):
        sum =0
        for val in self.marks:
            sum +=val
        print("Hi :",self.name, "Your Average score is :",sum/3)
s1 = Student("Ram",[99,100,98])
s1.average()