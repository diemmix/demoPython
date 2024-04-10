import pandas as pd
# Read data from CSV file into DataFrame
csv_data = pd.read_csv('E:/BPS/PyCharm/DemoPython/.idea/my_data.csv')
# Display some data to check
print(csv_data.head())

csv_data.to_csv('E:/BPS/PyCharm/DemoPython/.idea/my_data.csv', index=False)