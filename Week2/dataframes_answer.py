import pandas as pd

# Part 1: Create DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df1 = pd.DataFrame(data)
print("Part 1 - DataFrame:")
print(df1)
print("\n")

# Part 2: Indexing and Accessing Columns
# Accessing the "Age" column
print("Part 2 - Accessing 'Age' column:")
print(df1['Age'])
print("\n")

# Accessing the first row (person named John)
print("Part 3 - Accessing first row (John):")
print(df1.iloc[0])
print("\n")

# Part 3: Adding a New Column
# Adding a new column 'Salary'
df1['Salary'] = [50000, 60000, 55000, 45000]
print("Part 4 - Adding 'Salary' column:")
print(df1)
print("\n")

# Part 4: Modifying Data
# Modify the city of 'Peter' to 'Madrid'
df1.loc[df1['Name'] == 'Peter', 'City'] = 'Madrid'
print("Part 5 - Modifying 'City' of Peter:")
print(df1)
print("\n")

# Part 5: Filtering Data
# Filter people older than 30
filtered_df = df1[df1['Age'] > 30]
print("Part 6 - People older than 30:")
print(filtered_df)
print("\n")

# Part 6: Drop a Row
# Dropping the row where Name is 'Anna'
df1 = df1[df1['Name'] != 'Anna']
print("Part 7 - After dropping Anna:")
print(df1)
print("\n")

# Part 7: Sorting the DataFrame
# Sorting by 'Age' in descending order
sorted_df = df1.sort_values(by='Age', ascending=False)
print("Part 8 - Sorted by Age (descending):")
print(sorted_df)
