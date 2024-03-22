import pandas as pd

# To read the dataset

data = pd.read_csv('Salaries.csv',low_memory=False)

# First 10 rows of dataset

print(data.head(10))

print('---------------------------')

# Last 10 rows of dataset

print(data.tail(10))
print('---------------------------')

# To find the shape of our dataset

print(data.shape)
print('---------------------------')

# To get information about the dataset

data.info()
print('---------------------------')

# To find out the Null Values

print(data.isnull().sum())

print('---------------------------')

# To drop any data

print(data.columns)

dat = data.drop(['BasePay','Benefits','Notes'],axis=1)

print(dat)

print('---------------------------')

# To get the overall statistics about the dataframe

print(data.describe())
print('---------------------------')

# To find the top 5 occurences of the employee

print(data['EmployeeName'].value_counts())
print('---------------------------')

# To find out the unique job titles

print(data['JobTitle'].nunique())
print('---------------------------')

# To find total number of Job Title contain captain

print(data[data['JobTitle'].str.contains('CAPTAIN')])

print('---------------------------')

# To find the minimum maximum and average base pay

print(data['BasePay'].describe())
print('---------------------------')

# To find the job title of ALBERT PARDINI

print(data[data['EmployeeName']=='ALBERT PARDINI'],['JobTitle'])
print('---------------------------')

# Average Basepay of all the Employee per year

print(data.groupby('Year').mean()['BasePay'])
print('---------------------------')

# Top 5 most common jobs

print(data['JobTitle'].value_counts().head())