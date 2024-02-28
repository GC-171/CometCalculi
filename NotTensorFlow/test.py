import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the data
data = pd.read_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Data\NSL_Regular_Season_Data - NSL_Season_Data.csv")

# Drop non-numeric columns and the target column
X = data.drop(columns=['Winner', 'game_id', 'HomeTeam', 'AwayTeam', 'Home_Conference', 'Away_Conference'])
y = data['Winner']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate accuracy
test_accuracy = accuracy_score(y_test, y_pred)
print('Test accuracy:', test_accuracy)

# Add predictions to the DataFrame
X_test_df = pd.DataFrame(X_test, columns=X.columns)
X_test_df['Predicted_Winner'] = y_pred
X_test_df['Actual_Winner'] = y_test

# Export predictions compared to actual results to a CSV file
X_test_df.to_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Documents\TensorFlow2Results.csv", index=False)
