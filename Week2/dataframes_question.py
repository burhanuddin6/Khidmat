# Exercise: Pandas DataFrame Practice

import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

# Part 1: Create DataFrame
# 1. Create a DataFrame `df1` from the following dictionary:
#   Assign the dictionary to `df1` and print it.
#   Hint: Use pd.DataFrame(data)

# TODO: Write your code here

# Part 2: Indexing and Accessing Columns
# 2. Access the "Age" column of the DataFrame `df1` and print it.
#    Hint: You can use df1['Age'] to access the 'Age' column.

# TODO: Write your code here

# 3. Access the first row of `df1` (i.e., the data of the person named "John") and print it.
#    Hint: Use df1.iloc[0] to access the first row.

# TODO: Write your code here

# Part 3: Adding a New Column
# 4. Add a new column `Salary` to the DataFrame `df1` with the following values:
#    [50000, 60000, 55000, 45000].
#    Print the updated DataFrame.
#    Hint: You can add a new column using df1['Salary'] = [50000, 60000, 55000, 45000]

# TODO: Write your code here

# Part 4: Modifying Data
# 5. Modify the `City` of the person named "Peter" to "Madrid". Print the updated DataFrame.
#    Hint: Use df1.loc[df1['Name'] == 'Peter', 'City'] = 'Madrid' to modify the value.

# TODO: Write your code here

# Part 5: Filtering Data
# 6. Filter the DataFrame `df1` to show only people who are older than 30. Print the filtered DataFrame.
#    Hint: Use df1[df1['Age'] > 30] for filtering the data.

# TODO: Write your code here

# Part 6: Drop a Row
# 7. Drop the row corresponding to "Anna" from the DataFrame `df1` and print the updated DataFrame.
#    Hint: Use df1 = df1[df1['Name'] != 'Anna'] to drop a row.

# TODO: Write your code here

# Part 7: Sorting the DataFrame
# 8. Sort the DataFrame `df1` by the "Age" column in descending order and print the sorted DataFrame.
#    Hint: Use df1.sort_values(by='Age', ascending=False) to sort by Age.

# TODO: Write your code here
