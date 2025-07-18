import pandas as pd
import numpy as np


sal=pd.read_csv("C:\py notes\Fwd__pandas_exercises\Salaries.csv")
sal
sal.columns
print(sal.head())

print(sal.info())

sal.head().sort_values(by='BasePay')

averge_basepay=sal['BasePay'].mean()
print(averge_basepay)

highest_overtime=sal['OvertimePay'].max()
print(highest_overtime)

name='JOSEPH DRISCOLL'
Person_details=sal[sal['JobTitle']==name]
print(Person_details)

sal[sal['TotalPayBenefits']==name]
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']

#higest paid person
sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]

#lowest
sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]
sal.loc[sal['TotalPayBenefits'].idxmin()]

#average
sal.groupby('Year')['BasePay'].mean()

#unique job title
sal['JobTitle'].nunique()

## top 5 most common
sal['JobTitle'].value_counts().head(5)



sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)


























# Load the Salaries.csv file into a DataFrame
sal = pd.read_csv("C:\py notes\Fwd__pandas_exercises\Salaries.csv")

# Display the first few rows of the DataFrame
print(sal.head())import pandas as pd
import numpy as np

# Load the Salaries.csv file into a DataFrame
sal = pd.read_csv("C:\py notes\Fwd__pandas_exercises\Salaries.csv")

# Display the first few rows of the DataFrame
print(sal.head())

# Display information about the DataFrame
print(sal.info())

# Sort the DataFrame by 'BasePay' in ascending order
sal_sorted = sal.sort_values(by='BasePay')

# Calculate the average 'BasePay'
average_basepay = sal['BasePay'].mean()
print(f"Average Base Pay: {average_basepay}")

# Find the highest 'OvertimePay'
highest_overtime = sal['OvertimePay'].max()
print(f"Highest Overtime Pay: {highest_overtime}")

# Define the name to search for
name = 'JOSEPH DRISCOLL'

# Filter the DataFrame to find the person with the specified name
person_details = sal[sal['EmployeeName'] == name]
print(f"Details of {name}:")
print(person_details)

# Find the total pay benefits of the person
total_pay_benefits = sal.loc[sal['EmployeeName'] == name, 'TotalPayBenefits']
print(f"Total Pay Benefits of {name}: {total_pay_benefits.values[0]}")(f"Total Pay Benefits of {name}: {total_pay_benefits.values[0]}")
print(f"Total Pay Benefits of {name}: {total_pay_benefits.values[0]}")

# Display information about the DataFrame
print(sal.info())

# Sort the DataFrame by 'BasePay' in ascending order
sal_sorted = sal.sort_values(by='BasePay')

# Calculate the average 'BasePay'
average_basepay = sal['BasePay'].mean()
print(average_basepay)

# Find the highest 'OvertimePay'
highest_overtime = sal['OvertimePay'].max()
print(highest_overtime)

# Define the name to search for
name = 'JOSEPH DRISCOLL'

# Filter the DataFrame to find the person with the specified name
person_details = sal[sal['EmployeeName'] == name]
print(person_details)
