# Define a Circle class to creat a circle with radius r using the constructor. 
# Define an Area() method of the class which calculates the area of the circle. 
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle

class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
        
    def perimter(self):
        return 2* (22/7) * self.radius
        
cir1 = Circle(21)
print(cir1.area())
print(cir1.perimter())
        
        
        
        