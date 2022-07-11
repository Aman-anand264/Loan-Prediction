import pandas as pd
import numpy as np
warnings.filterwarnings("ignore")
train = pd.read_csv('dataset/train.csv')
train.head()
test = pd.read_csv('dataset/test.csv')
test.head()
train_original=train.copy()
test_original=test.copy()
train.columns

test.columns
