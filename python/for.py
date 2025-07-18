for i in range(0,8):
    print(i)

for i in range(1,9,2):
    print("*"*i)

for i in range(10,0,-2): 
    print(i)

for i in range(1,21):
     print("*"*i)

n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(n):
        print("*",end="  ")#end tke space b/n star has space
    print()
#increasing triangle    
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
#decreasing triangle
n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()
#right sided triangle*dicreasing space*increasing star
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

#right sided triangle*increasing space*decreasing star
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
            print("*",end=" ")
    print()
n=5
#hill pyramid,*dicreesing space,increasing star,increasing star
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
            print("*",end=" ")
    print()
#reverse hill pyramid,*increasing space,decreasing star,decreasing star
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
            print("*",end=" ")
    for j in range(i,n):
            print("*",end=" ")
    print()
#diamond pyramid*hill pyramid,reverse hill pyramid
n=5
for i in range(n-1):
    for j in range(i,n):
            print(" ",end=" ")
    for j in range(i):
            print("*",end=" ")
    for j in range(i+1):
            print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
          print(" ",end=" ")
    for j in range(n,(2*i)-1,-1):
         print("*",end=" ")
    
    print()
#dicresing space*increasing number
n=8
for i in range(0,9):
    for j in range(i,9):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()