# making attribute private

#class Person:
 #   __name ="ShreeRam"  # making this things conceputally private

#s1 = Person()
#print(s1.__name)

 #making methods private
class Person:
    __name ="ShreeRam"  # making this things conceputally private
    
    def __hello(self):
        print("Hello user")
        
    def welcome(self):
        self.__hello()

s1 = Person()
print(s1.welcome())