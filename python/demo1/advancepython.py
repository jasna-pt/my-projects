#counter with list
from collections import Counter
lst=[1,2,2,2,3,3,3,4,4,4,4,1,1,1,5,5]

Counter(lst)
#counter with string
from collections import Counter
str="hellohellohello"
Counter(str)

#counter with words in sentence
from collections import Counter
str="hello world hello world world world"

s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()

Counter(words)
#defaultdct
d={'name':'jasna','course':'python'}
d['name1']
from collections import defaultdict
d={'name':'jasna','course':'python'}
d=defaultdict(object)
e=defaultdict(lambda :10)
e['n']
e
d['a']
for item in d:
    print(item)
#namedtuple
from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])

sam = Dog(age=2,breed='Lab',name='Sammy')

frank = Dog(age=2,breed='Shepard',name="Frankie")
demo1=Dog(2,'p','f')
Dog
demo1
sam.breed
sam[2]
sam.age

#####date time
import datetime
t=datetime.time(4,30,10)
print(t)
print('hour  : ',t.hour)
print('minute: ',t.minute)
print('second: ',t.second)
print('microsecond: ',t.microsecond)
print('tzinfo: ',t.tzinfo)

print('earliast: ',datetime.time.min)
print('latest: ',datetime.time.max)
print('resolution: ',datetime.time.resolution)

today=datetime.date.today()
print(today)
print('ctime: ',today.ctime())
print('tuple: ',today.timetuple())
print('ordinal: ',today.toordinal())


print('year: ',today.year)
print('month: ',today.month)
print('day: ',today.day)
import datetime
d1 = datetime.date(2015, 3, 11)
print('d1:', d1)

d2 = d1.replace(year=1990)
print('d2:', d2)
d1-d2
d1-datetime.timedelta(year=5)

dir(d1)
dir(datetime.timedelta)
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%a"))

#py math
x=min(5,10,25)
y=max(5,10,25)
print(x)
print(y)
#abs()-absolute(+ve)
x=abs(-7.34)
print(x)
#pow(x,y)(x^y)
x=pow(4,3)
print(x)
#math.sqrt() square root
import math
x=math.sqrt(64)
print(x)
math.ceil(56/24)
56/24
56//24
dir(math)
math.sin(30)
import math
y=math.ceil(1.23)
x=math.floor(1.4)
print(y)
print(x)
#create file to compress
f = open("new_file.txt",'w+')
f.write("Here is some text")
f.close()
f = open("new_file2.txt",'w+')
f.write("Here is some text")
f.close()

#zipping file
import zipfile
import bz2file
import lzma
import os
os.getcwd()
comp_file1=zipfile.ZipFile('comp_file1.zip','w')
comp_file1.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file1.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file1.close()

#extracting from zip files
zip_obj = zipfile.ZipFile('comp_file1.zip','r')
zip_obj.extractall("extracted_content")

import zipfile
import bz2file
comp_fil4=zipfile.ZipFile('comp_file4.zip','w')
comp_fil4.write("new_file.txt",compress_type=zipfile.ZIP_BZIP2)
comp_fil4.write('loop.py',compress_type=zipfile.ZIP_BZIP2)
comp_fil4.close()


zip_obj=zipfile.ZipFile('comp_file4.zip','r')
zip_obj.extractall("extracted_content")


import shutil
directory_to_zip