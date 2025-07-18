light=input("light colour:")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")    
elif(light=="green"):
    print("go")
else:
    print("light is broken")


x=int(input("enter a number"))
if (x % 2==0):
    print("number is even")
else:
    print("number is odd")

a=int(input("enter  number"))
b=int(input("enter  number"))
c=int(input("enter  number"))
if a>b and a>c:
    print("a is the largest")
elif b>a and b>c:
    print("b is the largest")
else:
    print("c is the largest")
