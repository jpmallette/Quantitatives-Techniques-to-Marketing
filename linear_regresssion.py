
# taken from the book intro to statistical learning with application in R but apply to python
# purpose : Linear regression for inference

# configuration 
import pandas as pd
import matplotlib.pyplot as plt
from __future__ import division # to make sure it return a float
%pylab inline

# read and look at the data
data = pd.read_csv('C:\Users\Terry\Desktop\Project\TQM\TP2\linearRegression.csv')
data.head()

# is the type correct 
data.dtypes

# print the shape of the DataFrame
data.shape

# visualize the relationship between the features and the response using scatterplots
fig, axs = plt.subplots(1, 3, sharey=True)
data.plot(kind='scatter', x='fashion_innovativess', y='apparel_return', ax=axs[0], figsize=(16, 8))
data.plot(kind='scatter', x='buying_impulsiveness', y='apparel_return', ax=axs[1])
data.plot(kind='scatter', x='return_policy', y='apparel_return', ax=axs[2])


# create categorical data 



##########------------- validating if the hypothesis of the linear regression are respected ------# 


