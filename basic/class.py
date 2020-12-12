# name of class must be started with capital letter
class Claculator:
    def addition(x,y):
        add=x+y
        print(add)
    def subtraction(x,y):
        sub=x-y
        print(sub)
    def multipilication(x,y):
        mul=x*y
        print(mul)
    def division(x,y):
        div=x/y
        print(div)
Claculator.addition(20, 5)
Claculator.subtraction(20,5)
Claculator.multipilication(20,5)
Claculator.division(20,5)

# create a class named myClass
# __init is a first finction when a class is called and it is used to assign variables
# self is a first parameter of each functiob in class and is a refrence to current instance of the class
class MyClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greeting(self):
        print('you are {},{} years ols'.format(self.name,self.age))

p1=MyClass('behnaz',32) # create object of class
p1.greeting()
p1.name='Alireza'
p1.age=36
p1.greeting()