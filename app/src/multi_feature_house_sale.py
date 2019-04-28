# -*- coding: utf-8 -*-
"""multi_feature_house_sale.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LPdiMu9zKfEsg0Fx4dWSATE3uCLLp9Ud

House Sale Price Prediction:


https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python
"""

#load packages
import sys

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

import IPython
from IPython import display

import sklearn
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

import seaborn as sns

#misc libraries
import random
import time

#ignore warnings
import warnings
warnings.filterwarnings('ignore')


# Read the dataset from GitHub
url_train='https://raw.githubusercontent.com/tabchokkalingam/datasets/master/house-prices-advanced-regression-techniques/train.csv'
url_test='https://raw.githubusercontent.com/tabchokkalingam/datasets/master/house-prices-advanced-regression-techniques/test.csv'

train_full_ds=pd.read_csv(url_train)
test_full_ds=pd.read_csv(url_test)
chods=train_full_ds.sample(10)

train_full_ds.columns

#Select only the required Column.
f_cols=['LotArea','OverallQual', 'FullBath', 'YearBuilt']
p_cols=['SalePrice', 'LotArea','OverallQual', 'FullBath', 'YearBuilt']

trainds=train_full_ds[p_cols]
testds=test_full_ds[f_cols]

#scatterplot
sns.set()
sns.pairplot(trainds[p_cols], size = 2.5)
plt.show();

"""describe() - to see if there are 0 values. Min price must be >0.

Get the histogram to see,
*    Deviate from the normal distribution.
*    Have appreciable positive skewness.
*    Show peakedness.
"""

trainds.describe()

#Histogram - This gives the average max 'y' value. Here it is Avg Max SalePrice which is arnd 150000. 
plt.figure(figsize=(10,10))
plt.tight_layout()
sns.distplot(trainds['SalePrice'])

#Skewness and kurtosis
print("Skewness: %f" % trainds['SalePrice'].skew())
print("Kurtosis: %f" % trainds['SalePrice'].kurt())

#
X=trainds[f_cols].values
y=trainds['SalePrice'].values

#Splitting the test data - 80%-20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Training the algorithm
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting with the model
y_pred = regressor.predict(X_test)


print('Printing Actual vs Predicted values of Top 10 rows')
df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df.head(10))
print('-'*20)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

df1 = df.head(15)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

"""You can see that the value of root mean squared error is 4.19, which is more than 10% of the mean value of the percentages of all the temperature i.e. 22.41. This means that our algorithm was not very accurate but can still make reasonably good predictions."""