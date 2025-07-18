class Animal:
    name=""
    def eat(self):
        print("Ican eat")
class Dog(Animal):
    def display(self):
        print("My name is ",self.name)
labrador = Dog()

labrador.eat()
labrador.name="rohu"
labrador.eat()
labrador.display()


class Fruit:
    name=""
    def eat(self):
        print("favourite fruit is")
class Sweet(Fruit):
    def display(self):
        print("red colour fruit is ",self.name)
apple=Sweet()
apple.eat()
apple.name="woow"
apple.display()


class Circle:
    from math import pi
    def _init_(self,radius=1):
        self.radius=radius
    def setRadius(self,newradius):
        self.radius=newradius
        area=newradius*newradius*self.pi
        return area
    def getCircumference(self):
        return self.radius*self.pi*2
    
c=Circle()
print("radius is: ",c.radius)
print("area is: ",c.setRadius(5))


class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def display(self):
        print("name is:",self.firstname,self.lastname)
class student(Person):    
    pass
x=Person("JASNA","PT")
x.display()
X=student("afsal","c")
x.display()

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def display(self):
        print("name is:",self.firstname,self.lastname)
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)#same in it function both parent & child fun call parent -use super()
X=Student("jasna","pt")
X.display()
#add properties


####POLYMORPHISM
class Dog:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+"says woof!"
class Cat:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+"says meow!"

niko=Dog('niko')
felix=Cat('felix')
print(niko.speak())
print(felix.speak())

###SPECIAL METHOD
class Book:
    def __init__(self,title,author,pages):
        print("A book is created")
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return "Title: %s,author: %s,pages: %s"%(self.title,self.author,self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print("book is destroyed")

book=Book("python rocks!","jose portilla",159)
#special methods
print(book)
print(len(book))
#del book
del book
book.__len__()
print(book.__str__())

#function polymorphism
x="hello world"
print(len(x))
mytup=("apple","banana","cherry")
print(len(mytup))
#class polymorphism
class Car:
    def __init__(self,brand,model):
     self.brand=brand
     self.model=model

    def move(self):
     print("drive!")
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("sail!")
class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("fly!")

car1=Car("ford","mustang")
boat1=Boat("yacht","sailor")
plan1=Plane("boeing","747")
for x in (car1,boat1,plan1):
    x.move()
#inheritance polymorphism
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("moving...")
class Car(Vehicle):
    pass
class Boat(Vehicle):
        def move(self):
            print("sailing...")
class Plane(Vehicle):
    def move(self):
        print("flying...")
car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747") 
for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()    
class Student_data():
    def __init__(self,clgname):
        self.clgname=clgname
    def demo(self):
        print("beat institution")
class Student_id(Student_data):
    
    def __init__(self,name,rollno,clgname):
        super().__init__(clgname)
        self.name=name
        self.rollno=rollno
    def demo(self,rollno,**kwargs):
        super().demo()
        print("student id:  ",self.name,rollno)
        for key, value in kwargs.items():
            print(f"{key}: {value}")

std1=Student_id("jasna",22,"beat")
std2=Student_id("ezrin","21")
std1.demo(23,clgname="demo")
std1.clgname
std=Student_data("Beat")
std.demo()