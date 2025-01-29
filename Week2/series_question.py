import pandas as pd

# ===============================================
# Part 1: Creating a Pandas Series
# ===============================================

# Step 1: Create a simple Pandas Series
# TODO 1: Create a Pandas Series with the following values: [10, 20, 30, 40, 50]
#         and assign it to a variable called `s1`.
# Hint: Use `pd.Series()` function.

# Step 2: Create a Series with custom indexes.
# TODO 2: Create a Pandas Series with the following data: [100, 200, 300, 400]
#         and assign it to a variable called `s2`, but this time provide custom index labels.
#         Use the following indexes: ['a', 'b', 'c', 'd']
# Hint: Pass the `index` parameter while creating the Series.

# ===============================================
# Part 2: Accessing and Manipulating Data in Series
# ===============================================

# Step 3: Access a specific value.
# TODO 3: Access the value corresponding to the index 'c' in the `s2` Series.
# Hint: Use the index directly like `s2['c']`.

# Step 4: Perform arithmetic operations on Series.
# TODO 4: Add `s1` and `s2` element-wise, but first ensure that both Series have the same indexes.
# Hint: Use `.reindex()` if necessary to match the indexes.

# Step 5: Perform a mathematical operation on a Series.
# TODO 5: Multiply `s1` by 2 and print the result.
# Hint: You can multiply a Series by a scalar value directly.

# Step 6: Filter values in a Series based on a condition.
# TODO 6: Print all values in `s1` that are greater than 20.
# Hint: Use a condition like `s1 > 20` to filter the values.

# ===============================================
# Part 3: Additional Tasks
# ===============================================

# Step 7: Create a Series of squares of numbers from 1 to 5.
# TODO 7: Create a Series where the indexes are ['one', 'two', 'three', 'four', 'five'] 
#         and the corresponding values are the squares of the numbers 1 to 5.
# Hint: You can use a list comprehension or just hard-code the values.