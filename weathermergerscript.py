import os
import pandas as pd

# Path to the folder containing CSV files
folder_path = './combined'

# Initialize an empty DataFrame to store combined data
combined_data = pd.DataFrame()

# Iterate through each file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        # Merge the DataFrame with the combined DataFrame
        combined_data = pd.concat([combined_data, df], ignore_index=True)

# Assuming longitude, latitude, and date are common attributes
# You may need to adjust the column names accordingly
# Merge based on longitude, latitude, and date
combined_data = combined_data.groupby(['Longitude', 'Latitude', 'Date']).agg('sum').reset_index()

# Save the combined data to a new CSV file
combined_data.to_csv('combined_weather_data.csv', index=False)
