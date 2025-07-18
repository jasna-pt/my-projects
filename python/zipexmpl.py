#zip makes tuple of first elements, second elements, etc. of each list
x=(1,2,3,4)
y=(5,6,7,8)
z=(3,10,12)
list(zip(x,y,z))

#enumerate create tuple of index and value of each element in list
lst=['a','b','c','a']
print(list(enumerate(lst)))
for number,item in enumerate(lst):
    print(f'at index {number} is {item}')

try:
    a=int(input("value"))
except:
    print("invalid input")
    a=int(input("invalid input pls try again"))

try:
    f = open('testfile123','r')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("Error: Could not find file or read data")
except FileNotFoundError:
    print("data is invalid")
except ValueError:
    print("Syntax issue")
else:
    print("Content written successfully")
    f.close()
    
#finally
def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            print(val)
            break
        finally:
            print("Finally, I executed!")

##file
#             
askint() 
myfile = open(r'C:\Users\afsal\Downloads\demo.txt','r')
myfile.write('This is a new lineswer\n')
print(myfile)  
myfile.read() 
myfile.seek(0)  
myfile.close()      
my_file = open('test.txt','a+')
my_file.write('\nThis is text being appended to test.txt')
my_file.write('\nAnd another line here.')
my_file.seek(0)
my_file.read()
my_file.readlines()[2]
my_file.close()

