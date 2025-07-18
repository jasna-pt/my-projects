#####logical oparator
  
a=50
b=30
print(a>b)
print("AND Operator:",(a==b) and (a>b))

print("OR Operator:",(a==b) or (a>b))
print("NOT Operator:",not(a>b))
Val1= False
Val2= True
print(Val1 and Val2)
print(Val1 or Val2)
name=input("enter your name: ")
print("welcome",name)
val=input("enter a value: ")
print(type(val),val)
a=10
b=29
a+b
v=int(input("enter 1st numbers: "))
v=int(input("enter 2nd numbers: "))
print("sum of two numbers is:",v+v)

p=int(input("side of square: "))
print("area of square is:",p*p)

a=float(input("enter first float value: "))
b=float(input("enter second float value: "))
print("auvarage of float values is: ",(a+b)/2)

a=int(input("enter a number: "))
b=int(input("enter 2nd number: "))
print("or oparator:" , (a==b) or (a>b))
print("not opartor:",not(a>=b))
#loop
n=int(input("enter a number:"))
i=1
while i<=10:
    print(n*i)
    i +=1
#4qn
i=1
list=[]
while i<=10:
     print(i*i)
     list.append(i*i)
     i+=1
list
A=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx < len(A):
     print(A[idx])
     idx+=1 

B=['super man','spider man','iorn man','batman' ]
i=0
while i<len(B):
     print(B[i])
     i+=1
def cal_sum(a,b):
    sum=a+b
    print(sum)
    return sum
cal_sum(2,5)

def cal_sum(a,b):
     return a+b
cal_sum(56,78)


#oopps
class Account:
     def __init__(self,account_number,account_name):
          self.account_number=account_number
          self.account_name=account_name

Acc1=Account(12345,"jasna")
print(Acc1.account_number)
print(Acc1.account_name)


#inheritance
#single inheritance
class Car:
     colour="black"
     def start(self):
          print("car started")
     def stop(self):
          print("car stopped")
class Toyotacar(Car):
     def __init__(self,name):
          self.name=name
c1=Toyotacar("fortuner")
c2=Toyotacar("prius")          
print(c1.name)
print(c1.start())
print(c2.colour)

#multi_lavel inheritance
class Car:
     colour="black"
     def start(self):
          print("car started")
     def stop(self):
          print("car stopped")
class Toyotacar(Car):
     def __init__(self,brand):
          self.brand=brand
class Fortuner(Toyotacar):
     def __init__(self,type):
          self.type=type
car1=Fortuner("diesel")
car1.start()
#multiple inheritance
class A:
     varA="WELCOME TO CLASS A"
class B:
     varB="WELCOME TO CLASS B"
class C(A,B):
     varC="WELCOME TO CLASS C"
c1= C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

#  SUPER METHOD
class Car:
     def __init__(self,type):
          self.type=type
     def start(self):
          print("car started")
     def stop(self):
          print("car stopped")
class Toyotacar(Car):
     def __init__(self,name,type):
          super().__init__(type)###
          self.name=name
          
c1=Toyotacar("prius","electric")
print(c1.type) 


class student:
     def __init__(self,phy,chem,maths):
          self.phy=phy
          self.chem=chem
          self.maths=maths
     @property
     def percentage(self):
          return str((self.phy+self.chem+self.maths)/3)+"%"
stu=student(98,97,99)
print(stu.percentage)
stu.phy=86
print(stu.percentage)     
#
k=[1,2,3]
k.insert(2,45)
k.pop(2)
k
tup=(1,23,45,78)
tup.index(23)
#
Movies=[]
Movies.append(input("enter 1st favourite movie: "))
Movies.append(input("enter2nd favorite movie: "))
Movies.append(input("enter 3rd favourite movie: "))
print(Movies)
#
list1=[1,2,3,1]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
     print("palindrome")
else:
     print("not palindrome")