import tensorflow_decision_forests as tfdf
import pandas as pd

# Load the saved model
model_path = r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\NeuralNetwork\saved_model.pb"
model = tfdf.keras.RandomForestModel(model_path)

# Prepare new input data for prediction
new_data = {
    'HomeTeam': ['TeamA', 'TeamB'],  # Example home teams
    'AwayTeam': ['TeamX', 'TeamY']    # Example away teams
}

new_data_df = pd.DataFrame(new_data)

# Convert the new input data DataFrame to a TensorFlow dataset
new_ds = tfdf.keras.pd_dataframe_to_tf_dataset(new_data_df)

# Make predictions using the loaded model
predictions = model.predict(new_ds)

# Display the predictions
print("Predictions:")
print(predictions)
