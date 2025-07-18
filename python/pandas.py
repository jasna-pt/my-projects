import pandas 
a={'cars':["bmw","volvo","ford"],'passings':[3,6,9]}
myvar=pandas.DataFrame(a)
print(myvar)


import pandas as pd
a={'cars':["bmw","volvo","ford"],'passings':[3,6,9]}
myvar=pd.DataFrame(a)
print(myvar)

import pandas as pd

print(pd.__version__)


#SERIES
import numpy as np
import pandas as pd
labels=['a','b','c']
my_list=[10,20,30]
arr=np.array([10,20,30])
d={'a':10,'b':20,'c':30}
d
#***using list
pd.Series(data=my_list)
series=pd.Series(my_list,index=labels)
series
pd.Series(my_list,labels)
#*****numpy arrays
pd.Series(arr)
pd.Series(arr,labels)
###dictionary
pd.Series(d)

pd.Series(data=labels)

a1=pd.Series([1,2,3,4],index=['usa','germany','ussr','japan'])
a1
a2=pd.Series([1,2,5,6],index=['usa','germany','italy','japan'])
a2
a1+a2

x=["a","b","c"]
y=[1,2,3]
a=pd.Series(x,y)
a
e=[2,3,4]
b=pd.Series(x,e)
b
a+b

##data frame
import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)
randn(5,4)
df=pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns=' w x y z'.split())
df
df['w']
df[['w','z','x']]
df.w
type(df['w'])

#creat new column
df['new']=df['w']+df['x']
df

##removing column
df=df.drop('new',axis=1)#axis=0:row,axis=1:column
df
#REMOVED TO STORE-INPLACE
df.drop('new',axis=1,inplace=True)
df
#drop rows
df.drop('A',axis=0)
df.loc['A']###column name row
df.iloc[2]###index locate row
df.loc['B','y']
df.loc[['A','B'],['w','y']]

##conditional selection
df>0
df[df>0]
df[df['w']>0]
df[df['w']>0][['y']]
df[df['w']>0][['y','x']]
df[0]
df[(df['w']>0)&(df['y']>0)]
df[(df['w']>0)|(df['x']>0)] #or

#more index details
df
df.reset_index()


ab='hi guys good morning'.split()
ab
x='ca ny wy or co'.split()
df['states']=x
df['states1']=10


df.set_index('states')
df
df.set_index('states',inplace=True)
df
a=['G1','G1','G1','G2','G2','G2']
b=[1,2,3,1,2,3]
hier_index=list(zip(a,b))
hier_index=pd.MultiIndex.from_tuples(hier_index)
hier_index
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df
df.loc['G1']
df.loc['G1'].loc[[1]]
df.index.names=['group','num']
df.xs(1,level='num')



#########500 to 1000 random 100 values
import numpy as np
import pandas as pd
A=np.random.randint(500,1000,90)
b=A.reshape(15,6)
df3=pd.DataFrame(b,columns='w x y z u v'.split())
df3
b[6,3]
df3
b[10]
df3=pd.DataFrame(randn(6,5),index='A B C D E F'.split(),columns='w x y z u '.split())
df3['x']
df3.iloc[4]
df3.loc[2]
df3['t']=df3['w']+df3['y']
df3=df3.drop('t',axis=1)
df3
df3>600

df3[df3['w']>700]

######missing data
import numpy as np
import pandas as pd
df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})
df
df.dropna()
df.dropna(axis=1)
df.dropna(thresh=2)##2 NAN ELIMINATE

df.fillna(value='fill value')
df['A'].fillna(value=df['A'].mean())

#######GROUPBY
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
df
df.groupby('Company')['Sales'].sum()
S=df.groupby('Company')
S.mean(numeric_only=True)
S.describe()
S.count()
S.describe().transpose()
S.describe().transpose()['GOOG']
####
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])
df1
df2
df3
##concatenation
pd.concat([df1, df2,df3])
pd.concat([df1,df2,df3],axis=1)
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})    
left
right
pd.concat([left,right])
###merging
pd.merge(left,right,how='inner',on='key')#commom key

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                     'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})
left
right
pd.merge(left,right,how='inner',on=['key1','key2'])
pd.merge(left,right,on=['key1','key2'])#common
pd.merge(left,right,how='outer',on=['key1','key2'])#compine table
pd.merge(left,right,how='right',on=['key1','key2'])
pd.merge(left,right,how='left',on=['key1','key2'])



###joining
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
left.join(right)
right.join(left)
left.join(right,how='outer')
left.join(right,how='inner')


######operations
import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()
df['col2'].unique()
df['col2'].nunique()
df['col2'].value_counts()
df['col2'].value_counts().sort_index()
##applying finctions
def times2(x):
    return x*2
df['col1'].apply(times2)
df['col3'].apply(len)
df['col1'].sum()
##permenently deleting column
del df['col1']
df
##get column and index names
df.columns
df.index

df.sort_values(by='col2')
#null value
df.isnull()
#drop rows with nan values
df.dropna()
#filling NaN values 
import numpy as np
df = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()
df.fillna('FILL')

#### csv input
import pandas as pd
import numpy as np
import os
df=pd.read_csv(r'C:\py notes\pandas\example1.csv')
df
df.to_csv(r'C:\py notes\pandas\example1.csv',index=False)
df
#excel input
df=pd.read_excel("C:\py notes\pandas\Excel_Sample.xlsx",sheet_name='sheet1')
df
#excel output
df.to_excel("C:\py notes\pandas\Excel_Sample.xlsx")
df

####   HTML
df=pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
df[0].info()
df[1]