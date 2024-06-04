import pandas as pd

def load_csv_with_custom_headers(file_path):
    metadata = {}
    with open(file_path, 'r') as file:
        for i in range(1, 14):  
            line = file.readline().strip().replace('"', '')
            if ',' in line:
                key, value = line.split(',', 1)
                metadata[key.strip()] = value.strip()

    headers = pd.read_csv(file_path, skiprows=13, nrows=1).columns.tolist()  #
    units = pd.read_csv(file_path, skiprows=14, nrows=1).values.flatten().tolist() 
    combined_headers = [f"{header} ({unit})" if unit else header for header, unit in zip(headers, units)]

    data_df = pd.read_csv(file_path, skiprows=16, header=None)
    data_df.columns = combined_headers  

    return metadata, data_df


# Usage
file_path = 'samples/saurabh_gr86_Sonoma Race_a_0045.csv' #Put your thing here
metadata, data_df = load_csv_with_custom_headers(file_path)

print("Misc Info:")
for key, value in metadata.items():
    print(f"{key}: {value}")

print("\nData Sample:")
print(data_df.head())
