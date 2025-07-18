

def sum1():
    print("hello")
sum1()
a=sum1()
a
def sum2(name):
    print("hello "+name)

sum2("jasna")
a=sum2("pradeep")
a
type(a)

def sum3(name):
    return "hello "+name
print(locals())
a=sum3("pradeep")
a
list3=[1,2,3,4,5]
sum(list3)
def sum4(list6):
    sum=0
    print(locals())
    print(globals())
    for value in list6:
        sum=sum+value
    return sum
sum4(list3)

def product(list3):
    product=1
    for value in list3:
        product=product*value
    return product
product(list3)
evensum=0
oddsum=0
for value in range(1,100):
    if value%2==0:
        evensum=evensum+value
    else:
        oddsum=oddsum+value
evensum
oddsum

def result1():
    evensum=0
    oddsum=0
    for value in range(1,100):
        if value%2==0:
            evensum=evensum+value
        else:
            oddsum=oddsum+value 
    return evensum,oddsum
result1()

def result2(num1,num2):
    evensum=0
    oddsum=0
    for value in range(num1,num2):
        if value%2==0:
            evensum=evensum+value
        else:
            oddsum=oddsum+value 
    return evensum,oddsum
result2(1,200)

def result3(num1,num2):
    evencount=0
    oddcount=0
    value=num1
    while value<num2:
        if value%2==0:
            evencount=evencount+1
        else:
            oddcount=oddcount+1
        value=value+1
    return evensum,oddsum
    
result3(1,10)

def result(num1,num2):
    even=[]
    count1=0
    count=0
    odd=[]
    for i in range(num1,num2):
        if i%2==0:
            even.append(i)
            count+=1
        else:
            odd.append(i)
            count1+=1

    return even,odd,count1,count
result(2,25)


def calc_sum(a=0,b=0):
    sum=a+b
    print(sum)
    #return sum
a=calc_sum(8,7)
a
#tuple-arguments
def calc_sum(*args):
    print(args)
    result=sum(args)
    print(result)
    #return sum
calc_sum(4,5,6,9)
def calc_sum(*args):
    result=0
    for i in args:
        result=result+i
    return result
calc_sum(2,5,24)


def calc_product(*args):
    result=product(args)
    print(result)
calc_product(10,5,2,3)

def calc_multiple(*args):
    result=1
    for i in args:
        result=result*i
    return result
calc_multiple(5,6,2)
        



def calc_product(a,b):
    product=a*b
    print(product)
    return product
a=calc_product(9,8)
a
def calc_high(*args):
    max=args[0]
    for i in args:
        if i>max:
            max=i
    return max
calc_high(1,2,3,5)        

def calc_lowest(*args):
    min=args[0]
    for i in args:
        if i<min:
            min=i
    return min
calc_lowest(36,87,90,12,89,10)
#dictionarry-key word argument
def display(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key,":",value)
         

display(n="pradeep",m=25,c=78)
display(name="jasna",age=24,maths=45)

def display(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key,":",value)

display(name="jasna",course="python",center="beat")  

x={"name":"jasna","place":"pmna","course":"python","age":26}      

