import os
import shutil
source_pth = "C:/Users/arcot/OneDrive/Desktop/IISc/Hackathon Datasets/Copernicus Weather Data/"
dest_pth = "C:/Users/arcot/OneDrive/Desktop/IISc/Hackathon Datasets/Copernicus Weather Data/TotalPrecip"


for year_folder in os.listdir(source_pth):
    year_folder_path = os.path.join(source_pth, year_folder)
    if os.path.isdir(year_folder_path):
        for file in os.listdir(year_folder_path):
            if file.startswith("Total") and file.endswith(".csv"):
                source_file_path = os.path.join(year_folder_path, file)
                destination_file_path = os.path.join(dest_pth, file)
                shutil.move(source_file_path, destination_file_path)
                print(f"Moved {file} to {dest_pth}")