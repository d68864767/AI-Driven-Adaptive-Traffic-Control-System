```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

def load_processed_data(filename):
    """
    Load preprocessed data from a CSV file
    """
    df = pd.read_csv(filename)
    return df

def split_data(df):
    """
    Split data into training and testing sets
    """
    X = df.drop('congestion', axis=1)  # assuming 'congestion' is the target variable
    y = df['congestion']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Train a Random Forest model on the training data
    """
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model on the testing data
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model Mean Squared Error: {mse}")

def save_model(model, filename):
    """
    Save the trained model to a file
    """
    joblib.dump(model, filename)

def develop_model():
    """
    Load preprocessed data, train a model, evaluate it, and save the model
    """
    camera_data_df = load_processed_data('camera_data_processed.csv')
    sensor_data_df = load_processed_data('sensor_data_processed.csv')
    gps_data_df = load_processed_data('gps_data_processed.csv')

    # Combine all dataframes into one
    combined_df = pd.concat([camera_data_df, sensor_data_df, gps_data_df], axis=1)

    X_train, X_test, y_train, y_test = split_data(combined_df)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model, 'traffic_model.pkl')

if __name__ == "__main__":
    develop_model()
```

