import pandas as pd
# Create a data frame from a dictionary
data = {'Name': ['John', 'Emily', 'Sam', 'Sophia'],
 'Age': [25, 30, 18, 21],
 'City': ['New York', 'London', 'Paris', 'Tokyo']}
df1 = pd.DataFrame(data)
# Create a data frame from a list of lists
data = [['Apple', 1.2, 100],
 ['Banana', 0.5, 150],
 ['Orange', 0.8, 75],
 ['Mango', 1.5, 50]]
columns = ['Fruit', 'Weight', 'Price']
df2 = pd.DataFrame(data, columns=columns)
# Extract specific columns from dataframe
column1 = df1['column_name1'] # Extract a single column from df1
columns2 = df2[['column_name2', 'column_name3']] # Extract multiple columns from df2
# Extract specific rows from dataframe
rows1 = df1.loc[df1['column_name'] == 'value'] # Extract rows from df1 based on a condition
rows2 = df2.iloc[2:5] # Extract rows 2 to 4 from df2
# Merge or join dataframes based on a common key
merged_df = pd.merge(df1, df2, on='common_column') # Merge df1 and df2 based on a common 
column
# Concatenate dataframes vertically or horizontally
concatenated_df = pd.concat([df1, df2], axis=0) # Concatenate df1 and df2 vertically
concatenated_df2 = pd.concat([df1, df2], axis=1) # Concatenate df1 and df2 horizontally
# Group data by a column and perform aggregate functions
grouped_df = df1.groupby('column_name').sum() # Group df1 by column_name and sum the 
values
# Perform other operations on dataframes such as sorting, filtering, etc.
sorted_df = df1.sort_values('column_name') # Sort df1 based on column_name
filtered_df = df1[df1['column_name'] > 10] # Filter df1 based on a condition
# Access values using row and column indices
value = df1.iloc[0, 2] # Access value in the first row and third column of df1