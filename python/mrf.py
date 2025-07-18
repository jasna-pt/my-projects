#MAP,REDUCE AND FILTER

a=["JaSna","eZriN","fatHimA","afsAl","shahANa"]
for i in a:
    print(i[0])

def string1(a):
    return a[0]  

list(map(string1,a))

v=[1,67,85,90,34]
x=[1,2,3]
list(map(lambda b:b[0],a))
list(map(lambda a:a*a,x))
list(map(lambda b:b+b,x))
#
from functools import reduce
def sum1(a,b):
    return a+b
reduce(sum1,v)
reduce(lambda a,b:a+b,v)

from functools import reduce
def max1(a,b):
    return max(a,b)
reduce(max,v)
reduce(lambda a,b:max(a,b),v)




from functools import reduce
def val(a,b):
    if a>b:
        return a
    else:
        return b

reduce(val,v)

reduce(lambda a,b:a if a>b else b,v)

#FILTER

#Syntax: filter(function, sequence)
#Parameters:
#function: function that tests if each element of a sequence is true or not.
#sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.


# Define a function to check if a number is even
def is_even(n):
    return n % 2 == 0

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter to filter out even numbers
even_numbers = filter(is_even, numbers)
print("Even numbers:", list(even_numbers))  

def odd_fn(n):
    if n%2==1:
        return True
    else:
        return False
list(filter(odd_fn,numbers))



list(filter(lambda a:True if a%2==1 else False,numbers)  )   


x=[1,2,3,4,5,6]

list(map(lambda a:a*a,x))
list(map(lambda b:b+b,x))
list(map(lambda b:b+b,x))

for value in a:
    print(value)

reduce(lambda a,b:a if a>b else b,x)
reduce(lambda a,b:a if a<b else b,x)
reduce(lambda a,b:a<b,x)


list(filter(lambda a:True if a%2==0 else False,x))
list(filter(lambda a:a%2==0,x))
list(filter(lambda a:a%2==1,x))


a=["jasna","ezrin","fathima","afsal","shahana"]
for i in a:
   print(i.upper())
   
list(map(lambda b:b.upper(),a))   

a=["JaSna","eZriN","fatHimA","afsAl","shahANa"]
for i in a:
    count=0
    for j in i:
        if j.isupper():           
            print(j)
            count+=1
    print(count)
    print("---------")

z=["APple","bANana","ORAnge","GRAPs","potATO"]
for i in z:
    count=0
    for a in i:
        if a.isupper():
           print(a)
           count+=1
    print(count)
    print(".......") 

color_list = ["Red","Green","White" ,"Black"]
for i in range(0,-2,-1):
    print(color_list[i])


color_list[0],color_list[3]


#Sample filename : abc.java
#Output : java
filename = "abc.java"
print(filename[4:])

ext=["bfk.cjc","nxjAJ.dgsjdsj","ZsHAF.ZXnZ"]
filename.index(".")
for value in ext:
    print(value[value.index(".")+1:])

#10. Write a Python program that accepts an integer (n), n+nn+nnn.

n=input("enter a number")
n=5
n=str(n)
nn=n+n
nnn=n+n+n
nnn
int(n)+int(nn)+int(nnn)

int(n)+int(n+n)+int(n+n+n)


print("jasna \n pt")

a=12
c=[12,23]
type([])
b="jasna"
type(b)
dir(b)
type(a)
dir(a)
b.upper()
