class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def demo(self):
        print("hello "+self.name)

obj1=Person("jasna",24)
obj2=Person("Pradeep",28)
obj3=Person("xyz",33)
dir(obj3)
obj2.demo()
obj1.name
obj2.name

#
class fruits:
    pass
apple=fruits()
type(apple)
dir(apple)
#
class Dog:

    def __init__(self, name,colour):
        self.name=name
        self.colour=colour
    def demo(self):
        print("the dog name is "+self.name)
        print("dog colour is "+self.colour)
obj1=Dog("mimi","black")
obj2=Dog("mox","brown")
obj3=Dog("acd","red")
obj4=Dog("xxx","yellow")
obj3.demo()
obj1.demo()

#
class Dog1:
    attr1="mammal"
    attr3="dog"
    def __init__(self,attr2):
        self.attr2=attr2
        
    def fun(self):
        print("dog is a "+ self.attr1)
        print("dog is a "+self.attr2)
obj1=Dog1("mammal1")
obj2=Dog1("pet")
obj1.fun() 
obj1.attr2    
y=[12,23,34,45,56,67,78]
for val in x:
    sum(x)



i=0
for value in x:
    i=i+value


def sum(x):
    i=0
    for value in x:
        i=i+value
    return i
    
sum(y)-200

class Demo():
    def sum(self):
        i=0
        x=[12,23,34,45,56,67,78]
        for value in x:
            i=i+value
        return i
    
a=Demo()
a.sum()-100

class Demo():
    def sum(self,x):
        i=0
        for value in x:
            i=i+value
        return i
    
b=Demo()
b.sum(y)

class Demo():
    def __init__(self,x):
        self.x=x
    def sum(self):
        i=0
        for value in self.x:
            i=i+value
        return i

c=Demo(y)
c.sum()
#py prgrm to count the no.of each charecter in a list
v=['aab','aac','bba','dad']
for i in v:
    (i.count('a'))

def calc_count(v):
    count=0
    for value in v:
        count=count+value.count('a')
    return count
           
calc_count(v)    


class Count():
    def calc_count(self,v):
        count=0
        for value in v:
            count=count+value.count()
        return count
    def calc_count1(self,v,x):
        count=0
        for value in v:
            count=count+value.count(x)
        return count
    
demo=Count()
demo.calc_count1(v,'a')

c=['aaab','bbc','ccd','dde']
for i in c:
    count=0
    for value in i:
        count=count+1
    print(i,count)


def calc_count1(c):
    for i in c:
        count=0
        for value in i:
          count=count+1
        print(i,count)
calc_count1(c)    


class Number():
    def calc_count1(self,c):
        for i in c:
            count=0
            for value in i:
              count=count+1
            print(i,count)
demo=Number()
demo.calc_count1(c)




class Number():
    def __init__(self,c):
        self.c = c
    def calc_count1(self):
        for i in self.c:
            count=0
            for value in i:
                count=count+1
            print(i,count)

d=['aaab','bbc','ccd']
class Number():
    def __init__(self,c):
        self.c = c
    def calc_count1(self):
        result=[]
        for i in self.c:
            count=0
            for value in i:
                count=count+1
            result.append((i,count))
        return result

s=Number(d)
s.calc_count1()


d=['aaab','bbc','ccd']
class Number1():
    def __init__(self,c):
        self.c = c
    def calc_count1(self):
        
        
        for i in self.c:
            count=0
            for value in i:
                count=count+1
            print(i,count)
s=Number1(d)
s.calc_count1()


for i in range(1,7):
    for j in range(1,2*i):
        print("*",end="")
    print("")
def fun():
    for i in range(1,7):
        for j in range(1,2*i):
            print("*",end="")
        print("")
fun()            

class Pattern():
    def fun(self):
      for i in range(1,7):
        for j in range(1,2*i):
            print(" * ",end=" ")
        print("")

demo=Pattern()
demo.fun()

class Student():
    def __init__(self, name, age, gender):
        self.name = name
        self.age=age
        self.gender=gender
    def display(self):
        print("Name:", self.name)
        print("age:",self.age)
        print("gender:",self.gender)

stud1=Student("jasna",26,"female")
stud2=Student("ezrin",4,"female")
stud3=Student("afsal",32,"male")
stud1.display()
stud3.display()
stud2.display()


class Prod():
    def __init__(self,j):
        self.j=j
    def demo(self):
        pro=1
        for i in self.j:
            pro=pro*i
        return pro
j=[12,23,34,45,56]    
value=Prod(j)
value.demo()

for i in range(7,0,-1):
    for j in range(7-i):
        print("*",end="")
    print("")


class Sum():
    def __init__(self,h):
        self.h=h
    def demo(self):
        sum=0
        for i in self.h:
            sum=sum+i
        return sum
h=[10,20,30,40]    
v=Sum(h)
v.demo()    

class Oddeven():
    def __init__(self,odd,even):
        self.odd=odd
        self.even=even
    def demo(self):
        odd=0
        even=0
        for i in range(1,50):
            if i%2==0:
                even=even+i
            else:
                odd=odd+i
        return odd,even
x=Oddeven(1,50)
x.demo()
 
class Abc():
    def calc_sum(self,*args):
        print(args)
        result=sum(args)
        return result
x=Abc()
x.calc_sum(23,45,87,90,43)


class Xyz:
    def calc_product(self,*args):
        result=1
        for i in args:
            result=result*i
        return result
r=Xyz()
r.calc_product(23,10,67,90,100)   
    

a="pradeep"
print("%r"%a)

b=89
print("%.3f"%b)