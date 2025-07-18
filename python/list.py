mylist=['a string',3,5,78]
len(mylist)
mylist[0]
mylist[3]
mylist[1: ]#index 1
mylist[ :3]#upto index3
mylist+[4,67,78]

mylist *2 #make the list double
list1=[1,2,3,4,5] 
list1
dir(list1)
list1.append([99,100])#.append to add SINGLE ELEMENT to end of the list
list1
list1[-1][0]

list1.pop(0)

list1
list1[1]
new_list = ['a','e','x','j','b']
new_list.reverse()  #reversing the list
new_list
new_list.sort()
new_list

new_list1=[1,2,3,4,5]
new_list1.reverse()
new_list1
new_list1.sort(reverse=True)#true sorted to descending order
new_list1

list5=[45,56,32]
list5.sort()
list5
list5.sort(reverse=True)
list5


list9=[56,77,99,100]
list9.extend((56,99))
list10=[1,2,3,4]
list9.extend(list10)
list9

#NESTING LIST
A=[1,2,3]
B=[4,5,6]
C=[7,8,9]
MATRIX=[A,B,C]
MATRIX #NESTING
MATRIX[0]
MATRIX[0][2]
MATRIX[1][2]
MATRIX[2]


x={1,3,3,4,5}
x
type(x)
dir(x)
x.add(0)
x[0]
y={"apple","banana",0,1,2,True}#true=1,false=0[treated as duplicate]
y
len(y)
type(y)

z=set(('hello','guys','mango',))  #USE DOUBLE ROUND BRACKET set()constructor to make set
z

#BOOLEAN

print(True and False)
print(True or False)
print(not False)
3>5
10>5
b = None
print(b)
a=True
a=500
b=700
if b>a:
    print("b is greater than a")
else:
     print("b is not greater than a")
print(bool("hello"))
print(bool(15))