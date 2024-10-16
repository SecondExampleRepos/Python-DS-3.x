import pandas as pd
from typing import TypedDict, Required

class Metadata(TypedDict):
    key: Required[str]
    value: Required[str]

def load_csv_with_custom_headers(file_path: str) -> tuple[Metadata, pd.DataFrame]:
    metadata: Metadata = {}
    try:
        with open(file_path, 'r') as file:
            for i in range(1, 14):  
                line = file.readline().strip().replace('"', '')
                if ',' in line:
                    key, value = line.split(',', 1)
                    metadata[key.strip()] = value.strip()

        headers = pd.read_csv(file_path, skiprows=13, nrows=1).columns.tolist()
        units = pd.read_csv(file_path, skiprows=14, nrows=1).values.flatten().tolist()
        combined_headers = [f"{header} ({unit})" if unit else header for header, unit in zip(headers, units)]

        data_df = pd.read_csv(file_path, skiprows=16, header=None)
        data_df.columns = combined_headers

        return metadata, data_df

    except (FileNotFoundError, pd.errors.EmptyDataError) as e:
        e.add_note("Ensure the file path is correct and the file is not empty.")
        print(f"Error loading CSV file: {e}")
        return {}, pd.DataFrame()
