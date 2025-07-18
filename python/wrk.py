A=["apple","mango",25,87,10,5.8,True]
A[0:2].upper()
A

print(A)
dir(A)
A[0].upper()
A
A[1].lower()
A.reverse()
A
type(A)
A.pop(1)
A.append(100)
A
len(A)
A[ : ]
A[1: ]
A[-1::-1]
A[-1 : :]


B=['dog','goat',45,1,2,3]
A.extend(B)
A
A+B
C=[45,88,99,100]
C.sort(reverse=True)
C
d=input()

a=["hello","guys","iam","jasna",56]
a[0]
a[1]
a[2]
a[3]
for i in a:
    print(i)

b=[1,2,3,"hello","guys","jasna"]
for value in b:
    print(value)


for index in range(0,len(a)):
    print(a[index])




for index in range(5,-1,-1):
    print(b[index])

"*"*5 
for i in range(1,6):
    print("*" * i)


  #case while  
    i=1
    while i<6 :
        print("*" * i)
        i +=1

for i in range(1,6):
    print(i)
# case while
i=1
while i<6 :
    print(i)
    i +=1

for row in range(1,6):
    for col in range(1,row+1):
        print(col,end=" ")
    print("")
#case while
row=1
while row<6:
    col=1
    while col<row+1:
        print(col,end=" ")
        col +=1
    print("")
    row+=1


n=int(input("enter the number of rows"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print("")
#case while
n=int(input("enter the number of rows"))
i=0
while i<n:
    j=0
    while j<i+1:
        print("*",end=" ")
        j +=1
    print("")
    i +=1
     
for i in range(1,6):
    for j in range(1,i+1):
        print(j," ",end="")
    print("")



x=[1,2,3,4,5,6,7,8,9]

for i in range(0,len(x)):
    print(x[i])
i=0
list2=[]
while i<len(x):
    print(x[i])
    list2.append(x[i])
    i+=1
list2
i=1
while i<9:
    print(i)
    i +=1

x=[1,2,3,4,5,6,7,8,9,]
for i in x:
    if i==6:
        break       #print after break-6 not included
    print(i)

list=['apple','banana','orange','grapes']
for i in list:
    if i=='banana':
       continue
    print(i)

n=int(input("enter a number"))
n=10
while n!=100:
    print(n)
    n=n+10
    










### wHILE LOOP ###
 
for i in range(1,7):
    for j in range(1,2*i):
        print("*",end="")
    print("")

list1=[1,2,3,4,5,6]
for index in range(0,len(list1)):
    print(list1[index])
 
index=0
while index<len(list1):
    print(list1[index])
    index=index+1

index=len(list1)-1
while index>=0:
    print(list1[index])
    index=index-1
i=1
while i<16:
    print(i)
    i += 2


i=1
while i<6:
    
    if i==3:
        i=i+1
        continue
    print(i)
    i=i+1


i=1
while i<6:
    print(i)
    i+=1
else:
      print("loop ended")

n=int(input("enter a number"))
while n!=0:
    print(n)
    n=int(input("enter a number"))

