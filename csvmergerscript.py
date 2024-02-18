import os
import pandas as pd

def merge_csv_files(directory, file_prefix):
    combined_data = []
    for filename in os.listdir(directory):
        if filename.startswith(file_prefix) and filename.endswith(".csv"):
            data = pd.read_csv(os.path.join(directory, filename))
            combined_data.append(data)

    if combined_data:
        combined_data = pd.concat(combined_data)
        combined_data.to_csv(f"combined_{file_prefix}_data.csv", index=False)
    else:
        print(f"No {file_prefix} data files found in the directory.")


file_prefix = "Temperature"
directory_path = f'C:/Users/arcot/OneDrive/Desktop/IISc/Hackathon Datasets/Copernicus Weather Data/{file_prefix}'
merge_csv_files(directory_path, file_prefix)
