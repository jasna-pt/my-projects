import numpy as np
list=[1,3,6,7]
list
x=np.array(list)
x
type(x)
my_matrix=[[1,2,3],[5,4,6],[7,8,9]]
my_matrix
np.array(my_matrix)

#arange
np.arange(1,10,2)
np.arange(0,10)
np.arange(1,25,5)
np.arange(10,1,-1)
np.arange(1,101).reshape(2,10,5)
np.arange(1,51).reshape(2,5,5)

#zeros and ones
x=np.zeros(3)
x
h=np.zeros((2,3))
h=np.ones((3,3))
h
ab=np.zeros((3,4))
ab
xy=np.ones((4,2,2,))
xy
#linspace-spaced numbers over a specified range
hi=np.linspace(0,10,5)
hi
g1=np.linspace(1,10,20)
g1

#EYE-Create an identity metrix
#eye(n)-create an n*n identity matrix
z=np.eye(5)
z
d=np.eye(2,3)
d

#random********rand(0 to 1)
q1=np.random.rand(2)
q1

np.random.rand(2)
np.random.rand(4,5)

#**********randn(-ve and +ve values)
q1=np.random.randn(2)
q1
f5=np.random.randn(4,4)
f5
#*********randint
e=np.random.randint(1,150)
e
f8=np.random.randint(1,150,5)
f8
np.random.randint(5,200,25)

##ARRAY ATTRIBUTES AND METHODS
ranarr = np.random.randint(0,50,10)
ranarr.size
ranarr.shape
ranarr.reshape(2,5)
ranarr
ranarr.shape=5,2
ranarr.min()
ranarr.argmin()
a=np.random.randint(0,50,40)
a.shape=(2,4,5)
a

xy=np.linspace(500,1000,50)
xy
xy.size
xy.shape=(2,5,5)
xy
d5=np.random.randint(500,1000,120)
d5
d5.reshape(3,5,8)
d5.shape=(3,5,8)
d5
d5.size

d5.dtype

x=d5[1,3, : ]
print(x)


e=np.arange(1,20,2)
e[5]
e [1:6]

###BROADCASTING
e[1:4]=50   #setting a value with  index range
e
g7=np.arange(1,30,3)
g7
slice_of_g7=g7[0:6]
slice_of_g7[:]=55
slice_of_g7

ja=np.array(([5,10,15],[20,25,30],[35,40,45]))
ja
ja[2]

#fancy indexing
hi=np.zeros((10,10))
hi
arr_length=hi.shape[1]
arr_length

for i in range(arr_length):
    hi[i]=i
hi
hi[[2,4,6,8]]
#selection
arr=np.arange(1,15)
arr>5
arr[arr>5]
#1
z=np.zeros((10))
z+5
#2
g=np.ones((10))
g
#3
d=np.arange(10,51)
d
#4
r=np.arange(10,51,2)
r
#5
met=np.arange(0,9)
met.shape=(3,3)
met
#6
import numpy as np
identity=np.eye(3,3)
identity
#7
ran=np.random.rand(1)
ran
#8
std=np.random.randn(5,5)
std
#9

e=np.arange(0.01,1.01,.01)
e.shape=(10,10)
e
#10(
ly=np.linspace(0,1,20)
ly.shape=(4,5)
ly
###indexing and selection
#1
h=np.arange(1,26).reshape(5,5)
h
#2
h[2:,1:]
h[3,4]
h[0:3,1:2]
h[4]
h[3:5]
h[1:3,1:]
h[0:3,0:2]
h[0:3,2:5]
h[3:5,2:]
three=np.random.randint(1,100,75)
three.shape=(3,5,5)
three
three[1,2:4,:]
three[0,3,:]+three[2,3,:]
three[0:3:2,3, : ]

###*****numpy operations
arr=np.arange(0,10)
arr+arr
arr*arr
h=np.array([55,60,65,70,75])
sum(h)
h.sum()
h.sum(axis=0)
h.sum(axis=1)
h.std()