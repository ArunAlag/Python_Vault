import os
import zipfile
from abc import ABC, abstractmethod

import pandas as pd

# 1) Define Blueprint
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path:str) -> pd.DataFrame:
        pass


# 2) Define the object
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path:str) -> pd.DataFrame:

        # Ensure the file is a zip file
        if not file_path.endswith(".zip"):
            raise ValueError("Zip File must end with .zip")

        # Extract the file and save it in a directory called extracted_data
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall("extracted_data")

        # Find the extracted CSV file
        extracted_files = os.listdir("extracted_data")
        csv_file = [file for file in extracted_files if file.endswith(".csv")]

        if len(csv_file) == 0:
            raise FileNotFoundError("No csv file found in the extracted_data")

        if len(csv_file) > 1:
            raise FileExistsError("Multiple csv files found in the extracted_data")

        # Convert the CSV file to DataFrame
        csv_file_path = os.path.join("extracted_data", csv_file[0])
        dataframe = pd.read_csv(csv_file_path)

        return dataframe

# 3) Implement the factory
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension:str) -> DataIngestor:
        if file_extension == "zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f"No ingestor available for {file_extension}")


# 4) User requesting factory to extract the file
if __name__ == "__main__":
    # Specify the file path
    file_path = ''

    # Determine the file extension
    file_extension = os.path.splitext(file_path)[1]

    # Get the correct ingestor
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    # Import the data and load the dataframe
    dataframe = data_ingestor.ingest(file_path)

    # Print the head of the dataframe
    print(dataframe.head())
    pass


