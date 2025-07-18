#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist

#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists

f=open("demofile.txt","r")
print(f.read())  # prints the content of the file
#Return the 5 first characters of the file:
f=open("demofile.txt","r")
print(f.read(5))

#You can return one line by using the readline() method:
f=open("demofile.txt","r")
print(f.readline())
print(f.readline())
f.close()

f=open("demofile.txt","a")
f.write("now the file has more content!")
f.close()
#open and read the file after appending
f=open("demofile.txt","r")
print(f.read())
f.seek(0)
import os
os.getcwd()
os.remove('test.txt')

#check if file exist
import os
if os.path.exists("test.txt"):
  os.remove("test.txt")
else:
  print("The file does not exist")

#delete entire folder os.rmdr methode
import os
os.rmdir("myfolder")
name="jasna"
name[0]
nam=iter(name)
next(nam)

for value in range(1,100):
  print(value)

def sum2(list1):
  list2=[]
  for value in list1:
    list2.append(value**2)
  return list2

sum2([1,2,3,4,5])

def sum3(list1):
  for value in list1:
    yield value**2

list(sum3([1,2,3,4,5]))

for value in sum3([1,2,3,4,5]):
  print(value)

#generstor function for the cube of numbers(power of 3)
def cube(n):
   for num in range(n): 
    yield num**3

cube(100)    
for x in cube(100):
  print(x)
  
