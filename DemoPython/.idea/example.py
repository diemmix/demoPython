import pandas as pd
#*** Create hypothetical data table with problems
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'Temperature': [25.3, None, 23.8, 26.5, 27.1],
    'Vibration': [0.02, 0.03, 0.01, 0.05, 999],
    'Pressure': [1012, 1010, 1013, 1011, 'High'],
    'Location': ['New York', 'Boston', 'Chicago', 'Los Angeles', 'Chicago']
}
# Creat DataFrame from data
df = pd.DataFrame(data)
# *** Export DataFrame
print(df)

 
#*** Remove lines containing missing values
df_cleaned = df.dropna()
print(df_cleaned)


#*** Remove outliers in the Vibration column
vibration_threshold = 100 
df_cleaned = df_cleaned[df_cleaned['Vibration'] < vibration_threshold]
print(df_cleaned)


#*** Convert the value 'High' in the Pressure column to NaN
df_cleaned['Pressure'] = pd.to_numeric(df_cleaned['Pressure'], errors = 'coerce')
#*** Remove rows containing NaN values
df_cleaned = df_cleaned.dropna(subset = ['Pressure'])
print(df_cleaned)

#*** Handle empty values in the 'Temperature' column
#*** Calculate the mean value of the 'Temperature' column (after removing previous empty values)
temperature_mean = df['Temperature'].mean()
#*** Fill the missing values with the mean value in the 'Temperature' column
df['Temperature'] = df['Temperature'].fillna(temperature_mean)
#*** Print the DataFrame after processing
print(df)

#*** Remove duplicate data
df.drop_duplicates(inplace=True)
