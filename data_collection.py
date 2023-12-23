```python
import os
import json
import requests

# Define the URLs or endpoints of your data sources
CAMERA_DATA_URL = "http://example.com/camera_data"
SENSOR_DATA_URL = "http://example.com/sensor_data"
GPS_DATA_URL = "http://example.com/gps_data"

def fetch_data(url):
    """
    Fetch data from a given URL
    """
    response = requests.get(url)
    data = response.json()
    return data

def save_data(data, filename):
    """
    Save data to a JSON file
    """
    with open(filename, 'w') as f:
        json.dump(data, f)

def collect_data():
    """
    Collect data from different sources and save them to local JSON files
    """
    camera_data = fetch_data(CAMERA_DATA_URL)
    save_data(camera_data, 'camera_data.json')

    sensor_data = fetch_data(SENSOR_DATA_URL)
    save_data(sensor_data, 'sensor_data.json')

    gps_data = fetch_data(GPS_DATA_URL)
    save_data(gps_data, 'gps_data.json')

if __name__ == "__main__":
    collect_data()
```
