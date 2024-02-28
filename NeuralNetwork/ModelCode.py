import os
# Keep using Keras 2
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


dataset_df = pd.read_csv(r"C:\Users\rsen4\OneDrive\Desktop\Wharton Stuff\Data\NSL_Regular_Season_Data - NSL_Season_Data.csv")

HomeTeam = "HomeTeam"
AwayTeam = "AwayTeam"
Winner = "Winner"

ClassesHome = dataset_df[HomeTeam].unique().tolist()
ClassesAway = dataset_df[AwayTeam].unique().tolist()
ClassesWinner = dataset_df[Winner].unique().tolist()

dataset_df[HomeTeam] = dataset_df[HomeTeam].map(ClassesHome.index)
dataset_df[AwayTeam] = dataset_df[AwayTeam].map(ClassesAway.index)
dataset_df[Winner] = dataset_df[Winner].map(ClassesWinner.index)

def split_dataset(dataset, test_ratio=0.25, seed =1234):
  """Splits a panda dataframe in two."""
  np.random.seed(seed)
  test_indices = np.random.rand(len(dataset)) < test_ratio
  return dataset[~test_indices], dataset[test_indices]


train_ds_pd, test_ds_pd = split_dataset(dataset_df)
print("{} examples in training, {} examples for testing.".format(
    len(train_ds_pd), len(test_ds_pd)))

train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_ds_pd, label=Winner)
test_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_ds_pd, label=Winner)

# Specify the model.
model_1 = tfdf.keras.RandomForestModel(verbose=2)

# Train the model.
model_1.fit(train_ds)

Win_Features = [f.name for f in model_1.make_inspector().features()]
viz_model_1 = dtreeviz.model(model_1,
                           tree_index=3,
                           X_train=train_ds_pd[Win_Features],
                           y_train=train_ds_pd[Winner],
                           feature_names=Win_Features,
                           target_name=Winner,
                           class_names=ClassesWinner)
v = viz_model_1.view(scale=1.2)
v.show()
v.save("FirstTime.svg")

