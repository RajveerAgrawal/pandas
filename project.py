import pandas as pd

data = {
    'Id': [1, 2, 3, 4],
    'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'],
    'Role': ['CEO', None, None, None],
    'Salary': [100, 200, None, None]
}

df = pd.DataFrame(data)

print("Initial 2 values:\n", df.head(2))
print("Last 2 values:\n", df.tail(2))

null_count = df.isnull().sum().sum()
print(f"Total number of null values: {null_count}")

print("DataFrame Info:")
print(df.info())

df_drop_rows = df.dropna()
print("DataFrame after dropping rows with null values:\n", df_drop_rows)

df_drop_cols = df.dropna(axis=1)
print("DataFrame after dropping columns with null values:\n", df_drop_cols)

df['Salary'].fillna(300, inplace=True)
print("DataFrame after filling null values in Salary with 300:\n", df)

df['Role'].fillna('CEO', inplace=True)
print("DataFrame after filling null values in Role with 'CEO':\n", df)