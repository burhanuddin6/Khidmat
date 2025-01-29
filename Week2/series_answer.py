import pandas as pd

# ===============================================
# Part 1: Creating a Pandas Series
# ===============================================

# Step 1: Create a simple Pandas Series with the following values: [5, 10, 15, 20, 25]
#         and assign it to a variable called `s1`.

s1 = pd.Series([5, 10, 15, 20, 25])
print("Part 1 - Simple Series:")
print(s1)
print("\n")

# Step 2: Create another Pandas Series with custom indexes. 
#         Use the following data: [50, 100, 150, 200]
#         Assign it to a variable called `s2`, and use indexes ['a', 'b', 'c', 'd'].

s2 = pd.Series([50, 100, 150, 200], index=['a', 'b', 'c', 'd'])
print("Part 2 - Series with Custom Indexes:")
print(s2)
print("\n")

# ===============================================
# Part 2: Accessing and Manipulating Data in Series
# ===============================================

# Step 3: Access the value at index 'c' in the `s2` Series.

value_c = s2['c']
print("Part 3 - Accessing value at index 'c' in s2:")
print(value_c)
print("\n")

# Step 4: Add `s1` and `s2` element-wise. 
#         Make sure that the indexes in both Series match before performing the operation.

# First, let's reindex s1 to match the indexes of s2.
s1_reindexed = s1.reindex(['a', 'b', 'c', 'd', 'e'])
print("Part 4 - Adding s1 and s2 element-wise after reindexing:")
print(s1_reindexed + s2)
print("\n")

# Step 5: Multiply `s1` by 3.

s1_multiplied = s1 * 3
print("Part 5 - Multiply s1 by 3:")
print(s1_multiplied)
print("\n")

# Step 6: Filter out values in `s1` that are greater than 15.

filtered_values = s1[s1 > 15]
print("Part 6 - Filter values in s1 greater than 15:")
print(filtered_values)
print("\n")

# ===============================================
# Part 3: Additional Task
# ===============================================

# Step 7: Create a Series where the indexes are ['one', 'two', 'three', 'four', 'five']
#         and the values are the squares of the numbers 1, 2, 3, 4, 5. 
#         Assign it to a variable called `squares_series`.

squares_series = pd.Series([1, 4, 9, 16, 25], index=['one', 'two', 'three', 'four', 'five'])
print("Part 7 - Series of squares from 1 to 5:")
print(squares_series)