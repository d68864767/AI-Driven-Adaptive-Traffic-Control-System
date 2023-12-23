```python
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib

def load_processed_data(filename):
    """
    Load preprocessed data from a CSV file
    """
    df = pd.read_csv(filename)
    return df

def load_model(filename):
    """
    Load the trained model from a file
    """
    model = joblib.load(filename)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model on the testing data
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    print(f"Model Mean Squared Error: {mse}")
    print(f"Model Mean Absolute Error: {mae}")

def test_model():
    """
    Load preprocessed data, load the trained model, and evaluate the model
    """
    camera_data_df = load_processed_data('camera_data_processed.csv')
    sensor_data_df = load_processed_data('sensor_data_processed.csv')
    gps_data_df = load_processed_data('gps_data_processed.csv')

    # Combine all dataframes into one
    combined_df = pd.concat([camera_data_df, sensor_data_df, gps_data_df], axis=1)

    X = combined_df.drop('congestion', axis=1)  # assuming 'congestion' is the target variable
    y = combined_df['congestion']

    model = load_model('traffic_model.pkl')
    evaluate_model(model, X, y)

if __name__ == "__main__":
    test_model()
```
