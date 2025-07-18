import pandas as pd
import numpy as np

ecom=pd.read_csv("C:\py notes\Fwd__pandas_exercises\Ecommerce Purchases.csv")
ecom

ecom.head()

ecom.info()

ecom['Purchase Price'].mean()
ecom['Purchase Price'].max()
ecom['Purchase Price'].min()

len(ecom[ecom['Language']=='en'])

len(ecom[ecom['Job']=='Lawyer'])

ecom['AM or PM'].value_counts()

ecom['Job'].value_counts().head(5)

ecom[ecom['Lot']=='90 WT']['Purchase Price']

ecom[ecom['Credit Card']==4926535242672853]['Email']


len(ecom[(ecom['CC Provider']=='American Express' )& (ecom['Purchase Price']>95)])

ecom[(ecom['CC Exp Date']==2025).value_counts()]
sum(ecom['CC Exp Date'].apply(lambda a:a[3:])=='25')

ecom['Email'].apply(lambda a:a[a.index('@')+1:]).value_counts().head(5)


###########


ecom2=pd.read_csv("C:\py notes\ecommerce_product_dataset (1).csv")
ecom2
ecom2.head()
ecom2.info()
ecom2['Price'].mean()
ecom2['Price'].max()
ecom2['Price'].min()

ecom2['ProductName'].value_counts().head(5)
ecom2['Discount'].value_counts().head(6)
ecom2[ecom2['ProductName']=='Laptop']['DateAdded']
