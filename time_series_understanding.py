
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
import numpy as np

%matplotlib inline

series = pd.read_csv('C:/Users/KumarD1/Documents/international-airline-passengers.csv',
                     usecols = ["Month", "Passengers"])
series = series.dropna()
series.plot(    )
plt.show()

series.hist()
""" 
if data is stationary, the summary statistics should be consistent over time.
The mean should be consistent with a consistent variance indicating a Guassian
distribution. If the histogram does not show the guassian distribution then
it is an indication of non-stationary time series.
"""

X = series.Passengers
split = int(len(X)/2)
X1, X2 = X[0:split], X[split:]
mean1, mean2 = X1.mean(), X2.mean()
var1, var2 = X1.var(), X2.var()
print('mean1=%f, mean2=%f' % (mean1, mean2))
print('variance1 = %f, variance2 = %f' % (var1, var2))

"""
the mean and the variance are very different for first and second half
of the data which is another indicator of non-stationary
"""

# statistically to see stationarity of data is using Augmented Dickey-Fuller (ADF)test
"""
presence of unit root in a time series imply that the series is non-stationary.

ADF null hypothesis tests that a unit root is present in time series sample.
ADF statistic is a negative number and more negative it is stronger the rejection
of hypothesis that there is a unit root.

H0 (Null hypothesis): If accepted, suggests the time series has a unit root, 
meaning it is non-stationary.

H1 (Alternate hypothesis): The null hypothesis is rejected, it suggest time 
series does not have a unit root, meaning it is stationary.

p-value > 0.05 accept H0, implying data has unit root and is non-stationary.
p-value <= 0.05, reject H0, data does not have unit root and is stationary.

More negative ADF Statistic is the more likely we reject H0

"""

adf_test_result = adfuller(X)
print("ADF Statistic: %.4f" % adf_test_result[0])
print("p-value: %.4f" % adf_test_result[1])
print("Critical Values:")
for key, value in adf_test_result[4].items():
    print("\t %s : %.3f" %(key, value))

"""
In this time series the ADF statistic is positive and way above critical value
and also p-value is way above 0.05, so we can not reject H0. So data has a unit
root and is non-stationary.

"""
adf_test_result_log = adfuller(np.log(X))
print("ADF Statistic: %.4f" % adf_test_result_log[0])
print("p-value: %.4f" % adf_test_result_log[1])
print("Critical Values:")
for key, value in adf_test_result_log[4].items():
    print("\t %s: %.3f" %(key, value))

"""
After log tranformation the statistics has improved but still it is above 
implying we can't reject H0.Data still has still unit root and is non-stationary.

"""    
