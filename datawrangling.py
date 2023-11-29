import pandas as pd
# Sample data for two datasets
data1 = {
 'ID': [1, 2, 3],
 'Name': ['Alice', 'Bob', 'Charlie']
}
data2 = {
 'ID': [2, 3, 4],
 'City': ['London', 'Paris', 'Berlin']
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# Merging the two DataFrames based on 'ID'
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)
Data Aggregation - Grouping and Summarizing Data:
import pandas as pd
# Sample data for sales transactions

data = {
 'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
 'Amount': [100, 150, 200, 120, 180, 90]
}
df = pd.DataFrame(data)
# Grouping by 'Product' and calculating total sales
grouped_df = df.groupby('Product')['Amount'].sum()
print(grouped_df)
