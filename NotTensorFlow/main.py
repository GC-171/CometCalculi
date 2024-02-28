import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from keras.models import Sequential
from keras.layers import Dense

data = pd.read_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Data\NSL_Regular_Season_Data - NSL_Season_Data.csv")

encoder = LabelEncoder()
data['Winner'] = encoder.fit_transform(data['Winner'])

X = data.drop(columns=['game_id', 'Winner', 'HomeTeam', 'AwayTeam'])

y = data['Winner']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_numeric = scaler.fit_transform(X_train.select_dtypes(include=['float64', 'int64']))
X_test_numeric = scaler.transform(X_test.select_dtypes(include=['float64', 'int64']))

model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_numeric.shape[1],)),
    Dense(32, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train_numeric, y_train, epochs=10, validation_split=0.2, verbose=1)

test_loss, test_accuracy = model.evaluate(X_test_numeric, y_test, verbose=1)
print('Test accuracy:', str(test_accuracy * 100) + '%')

y_pred_prob = model.predict(X_test_numeric)
y_pred = y_pred_prob.argmax(axis=1)

y_pred_label = encoder.inverse_transform(y_pred)
y_test_label = encoder.inverse_transform(y_test)

results_data = {
    'Predicted_Result': y_pred_label,
    'Actual_Result': y_test_label
}
results_df = pd.DataFrame(results_data)

results_df.to_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Documents\TensorFlowResults.csv", index=False)


