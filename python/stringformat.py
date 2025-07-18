print("I'm going to inject %f here."%12 )
print("hai %1.3f"%3)
a="pradeep"
b="hari"
print("hello my name is %s \n %r"%(a,b))

a="pradeep"
print("I'm going to inject %r here." %a)


print('I once caught a fish %s.' %'this \tbig')
#I once caught a fish this      big.
print('I once caught a fish %r.' %'this \tbig')
#I once caught a fish 'this \tbig'.

print('Floating point numbers: %0.5f' %(13.144))

###############(string.format)
print('{0:8} | {1:8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:8}'.format('Apples', 3.))
print('{0:8} | {1:8}'.format('Oranges', 10))
print('{0:<8} | {1:8}'.format(1000,2))

print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))
####(fstring)
name1='12.3'
print(f"He said his name is {name1!r}")
 #Float formatting follows `"result: {value:{width}.{precision}}"`
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
print(f"My 10 character, four decimal number is:{num}")

print('{0:8} | {1:8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:8}'.format('Apples', 3.))
print('{0:8} | {1:8}'.format('Oranges', 10))
print('{0:8} | {1:8}'.format(1000,2))