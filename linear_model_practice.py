from sklearn import linear_model as lm
from sklearn import datasets
import numpy as np
import pandas as pd
# get the boston data from datasets module of sklearn package
data = datasets.load_boston()
# to get the feature variables use .feature_names and to get y or target variable
# use .target from the loaded data
data.feature_names; data.target

# create a pandas data frame of all the feature variables
df = pd.DataFrame(data = data.data, columns = data.feature_names)
target = pd.DataFrame(data.target, columns = ["MEDV"])

# Statmodels does not add a constant by default.
import statsmodels.api as sm
X =df["RM"]
y = target["MEDV"]

model = sm.OLS(y, X).fit()
predictions =  model.predict(X)
model.summary()
# as from the summary table we can see that by defualt the statsmodel lm
# does not provide constant, therefore we need to explicity define the constant
# using "sm.add_constant()" function

X = sm.add_constant(X)
model_with_cons = sm.OLS(y, X).fit()
predict1 = model_with_cons.predict(X)
model_with_cons.summary()

pd.DataFrame(data = {"Actual Y": y,"Predictions" : predictions,
                     "Predicition_with_cons" : predict1})
