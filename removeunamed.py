import os
import pandas as pd

def remove_useless_column(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate through each file
    for file_name in files:
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            feature_name = file_name.split('_')[1]
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            # Check if "useless" column exists
            if "Unnamed: 0" in df.columns:
                # Remove the "useless" column
                df.drop(columns=["Unnamed: 0"], inplace=True)
                df.rename(columns={"value": feature_name}, inplace=True)
                
                # Write the modified DataFrame back to the CSV file
                df.to_csv(file_path, index=False)
                print(f"Removed 'Unnamed: 0' column from {file_name}")
            else:
                print(f"'Unnamed: 0' column not found in {file_name}")
                df.rename(columns={"Value": feature_name}, inplace=True)
                df.to_csv(file_path, index=False)

# Provide the folder path containing CSV files
folder_path = "./combined"
remove_useless_column(folder_path)
