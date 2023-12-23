```python
import json
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(filename):
    """
    Load data from a JSON file
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def preprocess_data(data):
    """
    Preprocess data by converting it into a DataFrame and scaling the numerical features
    """
    df = pd.DataFrame(data)
    
    # Assume that the numerical columns need to be scaled
    numerical_cols = ['speed', 'density', 'flow']  # replace with your actual numerical columns
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    return df

def process_data():
    """
    Load and preprocess data from different sources
    """
    camera_data = load_data('camera_data.json')
    sensor_data = load_data('sensor_data.json')
    gps_data = load_data('gps_data.json')

    camera_data_df = preprocess_data(camera_data)
    sensor_data_df = preprocess_data(sensor_data)
    gps_data_df = preprocess_data(gps_data)

    # Save the preprocessed dataframes for further use
    camera_data_df.to_csv('camera_data_processed.csv', index=False)
    sensor_data_df.to_csv('sensor_data_processed.csv', index=False)
    gps_data_df.to_csv('gps_data_processed.csv', index=False)

if __name__ == "__main__":
    process_data()
```
