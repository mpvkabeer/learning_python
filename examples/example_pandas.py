import pandas as pd

# create a dictionary
data = {'Name': ['John', 'Alice', 'Bob'],
       'Age': [25, 30, 35],
       'City': ['New York', 'London', 'Paris']}

# create a dataframe from the dictionary
df = pd.DataFrame(data)

print(df)

#==========================#

# create a two-dimensional list
data = [['John', 25, 'New York'],
       ['Alice', 30, 'London'],
       ['Bob', 35, 'Paris']]

# create a DataFrame from the list
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])

print(df)


#==========================#

# create an empty DataFrame
df = pd.DataFrame()

print(df)


print('#==========================#')
# load data from a CSV file
df_from_csv = pd.read_csv('sample_data_large_set.csv')

#print(df_from_csv)

print(df_from_csv.info())  #desc table; column information
print(df_from_csv.head())  #First 5 records
print(df_from_csv.tail())  #Last 5 records
print(df_from_csv.describe()) #Showing Statistics




