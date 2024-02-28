import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Data\NSL_Regular_Season_Data - NSL_Season_Data.csv")

X = data.drop(columns=['Winner', 'game_id'])
y = data['Winner']

X = pd.get_dummies(X)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = RandomForestClassifier(random_state=42)
model.fit(X_scaled, y)

y_pred = model.predict(X_scaled)

accuracy = accuracy_score(y, y_pred)
print("Accuracy for full dataset:", accuracy)

predictions_df = pd.DataFrame({'Predicted_Winner': y_pred, 'Actual_Winner': y})
predictions_df.to_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Documents\TensorFlow3Results.csv", index=False)
