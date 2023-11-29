>>> df = pd.DataFrame([[np.nan, 2, np.nan, 0],
... [3, 4, np.nan, 1],
... [np.nan, np.nan, np.nan, np.nan],
... [np.nan, 3, np.nan, 4]],
... columns=list("ABCD"))
>>> df
 A B C D
0 NaN 2.0 NaN 0.0
1 3.0 4.0 NaN 1.0
2 NaN NaN NaN NaN
3 NaN 3.0 NaN 4.0
>>> df.fillna(0)
 A B C D
0 0.0 2.0 0.0 0.0
1 3.0 4.0 0.0 1.0
2 0.0 0.0 0.0 0.0
3 0.0 3.0 0.0 4.0
>>> df.fillna(method="ffill")
 A B C D
0 NaN 2.0 NaN 0.0
1 3.0 4.0 NaN 1.0
2 3.0 4.0 NaN 1.0
3 3.0 3.0 NaN 4.0
>>> values = {"A": 0, "B": 1, "C": 2, "D": 3}
>>> df.fillna(value=values)
 A B C D
0 0.0 2.0 2.0 0.0
1 3.0 4.0 2.0 1.0
2 0.0 1.0 2.0 3.0
3 0.0 3.0 2.0 4.0


import csv
def handle_missing_data(data):
 # Iterate over each row
 for row in data:
 # Iterate over each value in the row
 for key, value in row.items():
 if value == '':
 # Handle missing data (you can customize this part)
 row[key] = None
# Function to read data from CSV file
def read_csv_file(file_path):
 data = []
 with open(file_path, 'r') as file:
 reader = csv.DictReader(file)
 for row in reader:
data.append(row)
 return data
# Example usage
file_path = 'data.csv'
data = read_csv_file(file_path)
handle_missing_data(data)
# Print the processed data
for row in data:
 print(row)
