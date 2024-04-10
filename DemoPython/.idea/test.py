import pandas as pd

# Create DataFrame from hypothetical student data
data = {
    'ID': [101, 102, 103, 104, 105, 106, 107, 108, 101, 102],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Diem', 'Duong', 'Dung', 'Alice', 'Bob'],
    'Age': [20, 21, 22, 23, 24, 20, 21, 22, 23, 24],
    'Major': ['Math', 'Physics', 'Chemistry', 'Biology', 'Math', 'Physics', 'Chemistry', 'Biology', 'Math', 'Physics']
}
df = pd.DataFrame(data)

# Remove duplicate data based on 'ID' and 'Name' columns only
df.drop_duplicates(subset=['ID', 'Name'], inplace=True)

# Display DataFrame after removing duplicate rows
print(df)



