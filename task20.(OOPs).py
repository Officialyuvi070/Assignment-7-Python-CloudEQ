# 1. Create a class and make three object with different 
# parameters and change the values when you retrive 
# data from the class.

# Class example:

class Employee:
    def __init__(self,name,company,id,shift,age):# Declare the Constructor 
        self.name = name
        self.company = company
        self.id = id
        self.shift = shift
        self.age = age
      
    def get_salary(self,sal):# Declare the Function
        self.get_salary = sal

object=Employee("Yuvraj","CloudEQ",593,"day",23)
object.get_salary(500)
print(object.get_salary)
print(object.name)
print(object.company)
print(object.id)
print(object.shift)
print(object.age)

object1=Employee("Rahul","CloudEQ",556,"night",23)
object1.get_salary(400)
print(object1.get_salary)
print(object1.name)
print(object1.company)
print(object1.id)
print(object1.shift)
print(object1.age)

object2=Employee("Sunny","CloudEQ",567,"day",25)
print(object2.name)
print(object2.company)
print(object2.id)
print(object2.shift)
print(object2.age)

#. 2. Define the Class method and Super Method
# The super() function is used to give access to methods and properties of a parent or sibling class.
# A class method is bound to the class and not the object of the class. It can access only class variables.