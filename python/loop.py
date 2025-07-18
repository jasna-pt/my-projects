for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")    



for i in range(1,6):
    for j in range(6,i,-1):
        print(i,end=" ")  
    print("")


for i in range(1,6):
    for j in range(6,i,-1):
        print(5,end=" ")
    print("")    


for i in range(5,0,-1):
    for j in range(0,i+1) :
        print(j,end=" ")
    print("")
    
for i in range(1,6):
    for j in range(1,i+1):
        print(2*i-1,end=" ")
    print("")    


for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=" ") 
    print("")

for i in range(0,5):
    for j in range(i+1,0,-1):
        print(j,end=" ")  
    print("") 


for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ") 
    print("")    

for i in range(0,6):
    for j in range(5-i,0,-1):
        print(j,end=" ")
    print("")

a=0
for i in range(1,6):
    for j in range(1,i):
        print(a,end=" ")
        a=a+1    
    print("")


for row in range(1,6):
    for space in range(5,row,-1):
        print(" ",end=" ")
    for star in range(0,row):
        print(" * ",end=" ")
    print("")
