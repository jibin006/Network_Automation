import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Step 1: Load the data
def load_wireshark_data(file_path):
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    return df

# Replace with your CSV file path
wireshark_data = load_wireshark_data(r"C:/Users/jilub/OneDrive/Desktop/Demo.csv")

# Print column names to verify
print("Columns in DataFrame:")
print(wireshark_data.columns)

# Step 2: Preprocess the data
def preprocess_data(df):
    features = ['Length']  # Assuming 'Length' corresponds to 'frame.len'
    
    # Check which features are present
    missing_features = [feature for feature in features if feature not in df.columns]
    if missing_features:
        print(f"Warning: Missing columns {missing_features}")
    
    # Use .filter to only select the columns that are present
    df_selected = df.filter(items=[feature for feature in features if feature in df.columns])
    
    # Convert any relevant columns to numeric
    df_selected = df_selected.apply(pd.to_numeric, errors='coerce')
    
    # Drop any rows with missing values
    df_selected = df_selected.dropna()

    return df_selected

processed_data = preprocess_data(wireshark_data)

# Print processed data shape
print("Processed data shape:")
print(processed_data.shape)
print(processed_data.head())

# Step 3: Normalize the data
if not processed_data.empty:
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(processed_data)

    # Step 4: Train the anomaly detection model
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(scaled_data)

    # Step 5: Predict anomalies
    predictions = model.predict(scaled_data)

    # Step 6: Analyze and visualize results
    processed_data['anomaly'] = predictions

    normal = processed_data[processed_data['anomaly'] == 1]
    anomalous = processed_data[processed_data['anomaly'] == -1]

    plt.figure(figsize=(10, 6))
    plt.scatter(normal.index, normal['Length'], c='blue', label='Normal', alpha=0.5)
    plt.scatter(anomalous.index, anomalous['Length'], c='red', label='Anomaly', alpha=0.5)
    plt.xlabel('Index')
    plt.ylabel('Frame Length')
    plt.title('Network Traffic Anomaly Detection')
    plt.legend()
    plt.show()

    # Print summary
    print(f"Total packets: {len(processed_data)}")
    print(f"Detected anomalies: {len(anomalous)} ({len(anomalous)/len(processed_data)*100:.2f}%)")

    # Optional: Detailed look at anomalies
    print("\nSample of detected anomalies:")
    print(anomalous.head())
else:
    print("No data available for scaling and anomaly detection.")










