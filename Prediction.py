import os
os.environ['TF_USE_LEGACY_KERAS'] = '1'

import tensorflow_decision_forests as tfdf

import numpy as np
import pandas as pd
import tensorflow as tf
import datetime
import tf_keras
import math
import dtreeviz
from matplotlib import pyplot as plt
from IPython import display
import logging

logging.getLogger('matplotlib.font_manager').setLevel(level=logging.CRITICAL)
display.set_matplotlib_formats('retina') # generate hires plots
np.random.seed(1234)  # reproducible plots/data for explanatory reasons

def split_dataset(dataset, test_ratio=0.25, seed =1234):
    """Splits a panda dataframe in two."""
    np.random.seed(seed)
    test_indices = np.random.rand(len(dataset)) < test_ratio
    return dataset[~test_indices], dataset[test_indices]

Playoff = pd.read_csv('NSL_Group_Round_Games.csv')
dataset_df = pd.read_csv(r"NSL_Data.csv")
Winner = "Winner"

ClassesWinner = dataset_df[Winner].unique().tolist()
dataset_df[Winner] = dataset_df[Winner].map(ClassesWinner.index)

# train_ds_pd, test_ds_pd = split_dataset(dataset_df)

Playoff_ds = tfdf.keras.pd_dataframe_to_tf_dataset(Playoff)
# train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_ds_pd, label=Winner)
# test_ds = tfdf.keras.pd_dataframe_to_tf_dataset(test_ds_pd, label=Winner)
train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(dataset_df, label = Winner)


# Specify the model.
model_1 = tfdf.keras.RandomForestModel(verbose=2)

# Train the model.
model_1.fit(train_ds)

# model_1.compile(metrics=["accuracy"])
# evaluation = model_1.evaluate(test_ds, return_dict=True)
# print()

# for name, value in evaluation.items():
#   print(f"{name}: {value:.4f}")

classification_names = dataset_df[Winner].unique().tolist()
classification_names.sort()
print(classification_names)
prediction = model_1.predict(Playoff_ds)
class_predictions = list(map(lambda x: classification_names[x] , list(np.argmax(prediction, axis=1))))

print(prediction)
print(class_predictions)



