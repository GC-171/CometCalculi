import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Data\NSL_Regular_Season_Data - NSL_Season_Data.csv")

X = data.drop(columns=['Winner', 'game_id']) 
y = data['Winner']

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", accuracy)

predictions_df = pd.DataFrame({'Predicted_Winner': y_pred, 'Actual_Winner': y_test})
predictions_df.to_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Documents\TensorFlow2Results.csv", index=False)
