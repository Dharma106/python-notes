import pandas as pd
pd.set_option('display.float_format', lambda x: '%.4f' %x)
import numpy as np
from matplotlib import pyplot as plt
import os

folder_name = "Desktop\\.."
xlsx_file_name = "excel_file_name.xlsx"
path_loc = os.path.join(os.environ["USERPROFILE"], 
                        folder_name, xlsx_file_name)

actual_data = pd.read_excel(path_loc,
                            sheet_name = "data",
                            usecols = list(range(10)),
                            index_col ="Date")

actual_data.dropna(inplace=True)
#actual_data.set_index(actual_data.Date)
start_year_value = actual_data.Year >= 2011 
end_year_value = actual_data.Year <= 2019
req_filter = start_year_value & end_year_value

req_df = actual_data[req_filter]
nobs = 12
training_data = req_df[0:-nobs]
test_data =  req_df[-nobs:]

# Eliminating Trend and Seasonality
from statsmodels.tsa.seasonal import seasonal_decompose

req_var_vec = ['x1', 'x2','x3', 'x4']

req_var = "x1"
additive_deco = seasonal_decompose(training_data[req_var], model="additive")
#multiplicative_deco = seasonal_decompose(training_data[req_var],
#                                         model = "multiplicative")
plt.rcParams.update({"figure.figsize": (10,10)})
additive_deco.plot().suptitle('Additive Decompose', fontsize = 2)
# Extract the components
# Actual values = Sum of (Seasonal + Trend +  Residual)
df_decompsed = pd.concat([additive_deco.observed,additive_deco.seasonal, 
                          additive_deco.trend, additive_deco.resid], axis =1)
df_decompsed.columns = ['actual_values', 'seasonal', 'trend', 'residual']                          

## taking log transformation
##new_col = "Log_x1"
#new_col =  "log_x1"
#training_data.loc[:, new_col] = np.log(training_data[req_var])
#ma_log_colname = "moving_avg"+"_"+ new_col
#training_data.loc[:, ma_log_colname] = pd.DataFrame.rolling(
#        training_data[new_col],
#        window = 12).mean()
#
## removing seasonality and trend from transformed data
## this method is not adjustable to those period where we have high seasonality
#difference_col_name  = new_col+ "_" + "moving_avg_diff"
#training_data.loc[:, difference_col_name] = training_data[new_col] - training_data[ma_log_colname]
#stationary_test(training_data, difference_col_name)

#%%
# checking the stationarity of time series                          
from statsmodels.tsa.stattools import adfuller

def stationary_test(data, column_name, signif = 0.05,
                    graphical_output = False):
    
    if graphical_output == True:
        rolling_mean = pd.DataFrame.rolling(data[column_name],
                                            window = 12).mean()
        rolling_sd = pd.DataFrame.rolling(data[column_name],
                                          window = 12).std()
        plt.figure(figsize = (10,6))
        plt.plot(data[column_name],
                 color = "blue", 
                 label = "Actual %s" %column_name)
        plt.plot(rolling_mean,
                 color = "red",
                 label = "Rolling Mean")
        plt.plot(rolling_sd,
                 color = "black",
                 label = "Rolling Std")
        plt.legend(loc = "best")
        plt.title("Actual, Rolling Mean and Standard Deviation")
        plt.show(block =  False)         
    # stationary of data is being evaluated.
    # H0: the time series has unit root test and it is non-stationary.
    # if p-value greater than 0.05 we fail to reject NULL hypothesis implying
    # data is has unit-root and it is non-stationary
    # adf_test_value = adfuller(training_data.RC_Export_MT,  autolag = "AIC" )
    # if test statistics is less than the critical value, we can reject 
    # Null Hypothesis say that ts is stationary
    # the ouput suggests that the series is non-stationary
    # the result can be verified taking the log transformation too.    
    def adjust_text(val, length=6): 
        return str(val).ljust(length)        
    adf_test_result = adfuller(data[column_name],
                              autolag = "AIC" )
    vec_round = np.vectorize(round)
    adf_test_output = pd.Series(vec_round(adf_test_result[0:4], 3),
                                index = ["ADF_Statistic",
                                         "p_value",
                                         "n_lags",
                                         "n_obs"])
    
    print(f'ADF test on "{column_name}"', "\n", "--"*35)
    print(f'Null Hypothesis: Series {column_name} has unit root. Non-Sationary.')
    print(f' Test-Statistic           = {adf_test_output["ADF_Statistic"]}')
    print(f' Significance Level       = {signif}')
    print(f' No. of Lags chosen       = {adf_test_output["n_lags"]}')
    print(f' No. of observation used  = {adf_test_output["n_obs"]}')
        
    for key, value in adf_test_result[4].items():
        print(f' Crritical value {adjust_text(key, 8)} = {round(value, 3)}')
    
    if adf_test_output["p_value"] <= signif:
        print(f' ==> P-Vlaue = {adf_test_output["p_value"]}. Reject Null Hypothesis.')
        print(f' ==> Implies Series is Stationary.')
    else:
        print(f' ==> P-Value = {adf_test_output["p_value"]}. Fail to reject Null Hypothesis.')
        print(f' ==> Series is Non-Stationary.')

stationary_test(training_data, req_var)
# for the test output which shows that data is non-stationary and
# this could be due to increasing/decreasing trend, existence of seasonality 
# in the series.
# the roll mean chart shows that we have an increasing trend and from the 
# actual data we can see the existence of seasonality too.

# testing seasonality of a time series
# use autocorrelation funciton plot (ACF plot). If the series has
# a strong seasonal pattern it shows a definite repeated spikes at 
# multiples of the seasonal window.

# autocorrelation is simply the correlation of a series with its own lags. 
# if a series is significantly autocorrelated, that means the previous values 
# of the series would be helpful in predicting the current value.

# partial autocorrelation conveys the same but it conveys the pure correlation
# of a series and its lag, excluding the correlation contributions from
# the intermediate lags.

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
fig, axes = plt.subplots(1, 2, figsize = (12,3));

plot_acf(training_data[req_var], ax = axes[0]);
plot_pacf(training_data[req_var], lags =30, ax = axes[1])
 
# The plots and stationary test suggests series is not stationary as 
# p-value is greater than 0.05. 
# Taking first difference of the series.
training_data_differenced = training_data.loc[:, [req_var]].diff().dropna()

stationary_test(training_data_differenced, req_var)

# Lag Plots
# it's a scatter plot of a time series agains a lag of itself to check 
# existence of autocorrelation.
from pandas.plotting import lag_plot
fig_lag, axes = plt.subplots(1,4, figsize = (11,2), 
                                sharey = True);
for i, ax in enumerate(axes.flatten()[:4]):
    lag_plot(training_data[req_var], lag = i+1, ax = ax, c = "blue")
    ax.set_title("Lag" + str(i+1))

fig_lag.suptitle("Lag plots of "+ req_var, y = 1.10)
plt.show()    
# from the lag plot, we see that at lag1 there exists a relationship                                 


#***********************************
#       ************************************
# Vector Auto Regressive Model. This approach is used to analyse time 
# series where one series is impacting the others and the vice versa.


"""
Building a VAR model in Python
The procedure to build a VAR model involves the following steps:

1. Analyze the time series characteristics
2. Test for causation amongst the time series
3. Test for stationarity
4. Transform the series to make it stationary, if needed
5. Find optimal order (p)
6. Prepare training and test datasets
7. Train the model
8. Roll back the transformations, if any.
9. Evaluate the model using test set
10. Forecast to future

"""

from statsmodels.tsa.api import VAR
# from statsmodels.tsa.stattools import adfuller
from statsmodels.tools.eval_measures import rmse, aic

# visualize time series
def adjust_text(val, length=6): 
        return str(val).ljust(length)  
    
req_var_vec = ['RC_AB_FOB_diffs', 'uganda_scr15_RC_FOB_diffs',
               'vietnam_RC_scr16_fob_diffs', 'LIFFE_USD_MT']
df = training_data[req_var_vec]
fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (10,6));
for i, ax in enumerate(axes.flatten()):
    data = df[df.columns[i]]
    ax.plot(data, color = "blue", linewidth =1)
    ax.set_title(df.columns[i])
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.spines["top"].set_alpha(0)
    ax.tick_params(labelsize =6)
plt.tight_layout();

# Testing Causation using Granger’s Causality Test
# the hypothesis formed in the Granger's casuality test is that the 
# coefficient of past values in the regression equation is zero.
# i.e past value of time series x2 does not cause the other series x1.
# reject the Null hypothesis if p-value of the test is less than significance level
# of 0.05. It means we reject the hypothesis of x2 does not causes x1.

from statsmodels.tsa.stattools import grangercausalitytests
def granger_casuation_matrix(data, variables, 
                             test = "ssr_chi2test", 
                             max_lag = 12,
                             verbose = False):
    """
    check granger-casuality of all possible combination of the time-series.
    The rows are response variable, columns are predictors. The output table
    contains p-value.
    P-value less than significance level,  implies (Null-hypothesis) that 
    the coefficients of the corresponding past values is not zero and the 
    X2 does not casue X1 can be rejected.
    """
    tot_vars = len(variables)
    # create a dataframe of dimension variables * variables to store p-value
    df = pd.DataFrame(np.zeros((tot_vars, tot_vars)), 
                      columns = variables, index = variables)
    
    for cols in df.columns:
        for rows in df.index:
            gc_test = grangercausalitytests(data[[rows, cols]],
                                            maxlag = max_lag, 
                                            verbose = False)
            # store p-values for each lag as list for the specified test-type
            # defualt gives all the four test 2 based on f & 2 based on chi2
            
            p_values = [round(gc_test[lag+1][0][test][1], 4) 
                        for lag in range(max_lag)]
            if verbose: print(f'Y = {rows}, X= {cols}, P Values = p_values')
            min_p_value = np.min(p_values)
            df.loc[rows, cols] = min_p_value
    df.columns = [var + '_x' for var in variables]
    df.index = [var + '_y' for var in variables]
    print(f"Returned a Minmum P-Value table from the lag used till {max_lag}")
    return df
     
# evaluate whether one time series causes other or not
# output of below will be p-value matrix    
granger_casuation_matrix(training_data, req_var_vec)
# from the output matrix we see that except LIFFEE_USD_MT  
# is not cuased by india & uganda diffs
# we can bserve that all the variables (time series) except LIFFEE in the 
# system are interchangeably causing each other.

# Check the cointegration test.
"""
cointegration test helps to establish the presence of a statistically significant
connection between two or more time series.

cointegration can be understand by knowing "order of integration (d)"

Order of integration is nothing but the number of differencing required 
to make a non-stationary time series stationary.

So, when we have two or more time series, there exists a linear combination of
them that has an order of integration (d) less than that of the individual
series, then the collection of series is said to be cointegrated
 
"""    

from statsmodels.tsa.vector_ar.vecm import coint_johansen

def cointegration_test_result(data, num_lag_diff = 2):
    """
    Perform Johanson's Cointegration Test and Report Summary
    """
    output_coint = coint_johansen(data, -1, num_lag_diff)
    critical_val_dict = {"0.9" : 0, "0.95": 1, "0.99": 2}  
    # read each variable trace value
    traces_value = output_coint.lr1
    
    def adjust(str_char, lengtht = 6):
        return str(str_char).ljust(lengtht)
    max_char_len = max([len(var) for var in data.columns]) + 1

    # read the corresponding columns of critical values for each variable
    alpha_val = [0.10, 0.05, 0.01]
    print("\n Significance of granger-casuality at different critical values level.\n ")
    for alpha in alpha_val:
        coint_crit_val = output_coint.cvt[:, critical_val_dict[str(1-alpha)]]
        print(adjust("Name", max_char_len),
              " :: ", "Test Stat > C(%.1f%s)  =>    Signif \n"
              % ((1-alpha)*100, "%"), "---"*max_char_len)
        for col_name, trace, cvt in zip(data.columns,
                                        traces_value,
                                        coint_crit_val):
            print(adjust(col_name, max_char_len), " :: ",
                  adjust(round(trace, 2), 9), ">", 
                  adjust(cvt, 8), " => " , trace > cvt)
        print("\n")


# johanson's co-integration test
cointegration_test_result(training_data[req_var_vec], num_lag_diff=12)    
# once we statistically get to understand the existence of cointegration
# we can move to next step of modelling.
        
# VAR modelling assumes that time serie we want to estimate is stationary.
# so it's necessary to check all the time series in the system is stationary.
        
# if a series is found to be non-stationary, you make it stationary by 
# differencing the series once and repeat the test again until it becomes stationary.
      
# adf-test stationary check for all the series of interest.
for variable in req_var_vec:
    stationary_test(training_data, variable)
    print("\n")
    
# the adf_test suggest that except LIFFE_USD_MT others are stationary
# from the cointegration and granger test we did see that LIFFE_USD_MT
# series is not have influence so dropping this variable.
req_var_vec_mod = req_var_vec[0:3]

# the other approach would be to take first differenced data and
# again check for stationarity
# ADF test on first differenced dataframe
first_diff_df = training_data[req_var_vec].diff().dropna()
for var in req_var_vec:
    stationary_test(first_diff_df, var)
    print("\n")

# using VAR method to fit the model and to select the right order of 
# auto-regressive (p) we can test the model at different lag order and
# choose that order which gives least AIC value.
    
model = VAR(first_diff_df[req_var_vec])
# automatic selection of optimal lag
each_lag_summary = model.select_order(maxlags =12)
print(each_lag_summary.summary())

# manula testing for 12 lag and deciding by chossing low AIC value
for lag in list(range(1,12)) :
    result = model.fit(lag)
    print('Lag order = ', lag)
    print('AIC : ', result.aic)
    print('BIC : ', result.bic)

# the AIC value at lag 3 and lag 7 shows the drop level meaning till
# lag3 the AIC value dropped and then from lag 4 it went up and again 
# at lag7 it showed similar phenomena.
# fitting the model at lag 1 as the AIC is minimum there.
fitted_model = model.fit(2)
fitted_model.summary()

# once optimal order of p is decided we can choose the fit for that particular
# order. Next we should check for serial correlation of Residuals/erros.
# this can be checked using Durbin Watson statistic. (it's done to see if
# there is any leftover pattern in the residuals.)

# if there exists any correlation left in residuals, it means there is some
# pattern in the series which still left to be explained by the model.
# In that case, either check by increasing the order of the model or include
# few more predictors into the system or look for a different algorithm to
# train the model.
# this check can be done by evaluating serial correlation. So to check 
# a commonly used measured is durbin-watson's statistic which is sum-squared
# differenc of lagged one error divided by sum-square of error.
# Darwin-Watson test value can varry from [0,4]. 
# the test value close to 2 suggest no significant correlation.
# closer to 0 implies +ve serial correlation
# closer to 4 implies -ve serial correlation.

from statsmodels.stats.stattools import durbin_watson
serial_corr = durbin_watson(fitted_model.resid)
max_char_len = max(list(map(len, req_var_vec)))
for col, val in zip(req_var_vec, serial_corr):
    print(adjust_text(col,max_char_len), "\t",":", round(val, 2))

#  the durbin-waston test results shows no existence of serious
# correlation for any of the series.
# forcast the future values and evaluating the test series
lag_order = fitted_model.k_ar

# to forecast for unseen data, we need end rows equal to lag values from 
# training_data. 
lagged_input_data = first_diff_df[req_var_vec].values[-lag_order:] 
frcst_output_data = fitted_model.forecast(lagged_input_data, 
                                          steps = nobs)


frcst_df_cols = [col + '_frcsted' for col in req_var_vec]    
frcsted_df = pd.DataFrame(frcst_output_data, 
                          index=req_df.index[-nobs:], 
                          columns=frcst_df_cols)

# once we estimate  forecasted value for required obs, need 
# to transfor to get the real forecast (as the forecast is done for 
# differenced data)

def transform_to_original(train_df, frcst_df, differenced_order):
    diff_ord_lst = list(range(1, differenced_order+1))
    diff_ord_lst.reverse()
    df_frcst_final = frcst_df.copy()
    train_col_name = train_df.columns
    frcst_col_name = df_frcst_final.columns
    for d in diff_ord_lst:
        for col1, col2 in zip(train_col_name,frcst_col_name):
            if d != 1:
                # roll back higher lagged difference
                df_frcst_final[str(col1)+f'_{d-1}diff'] = (
                    (train_df[col1].iloc[-(d-1)] - train_df[col1].iloc[-d]
                     ) + df_frcst_final[col2].cumsum()
                    )
            else:
                df_frcst_final[str(col2)+'_final'] = (
                    train_df[col1].iloc[-1] + df_frcst_final[col2].cumsum()
                    )
    
    return df_frcst_final

# transformed data output
output_df = transform_to_original(train_df=training_data[req_var_vec],
                                  frcst_df=frcsted_df,
                                  differenced_order=lag_order)

            
final_col = output_df.columns[4:]
forecast_df = output_df[final_col]

# plot the actual vs forecast
if len(req_var_vec) % 2 == 0:
    n_row = int(len(req_var_vec)/2)
    n_col = 2
    
fig, axes = plt.subplots(nrows= n_row, 
                         ncols=n_col, figsize = (11,9))              
for i, (col,ax) in enumerate(zip(req_var_vec, axes.flatten())):
    forecast_df[col+'_frcsted_final'].plot(
        legend=True, ax=ax).autoscale(axis='x',tight=True)
    test_data[col][-nobs:].plot(legend=True, ax=ax);
    ax.set_title(col + ": Forecast vs Actuals")
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.spines["top"].set_alpha(0)
    ax.tick_params(labelsize=6)    
    

# evaluating the forecast. Calculate different measures such as
# MAPE, ME, MAE, MPE, RMSE, corr and minmax

def forecast_accuracy_measures(actual_val, forecast_val):
    mape = np.mean(np.abs((forecast_val / actual_val)-1))
    me = np.mean(forecast_val- actual_val)
    mae = np.mean(np.abs(forecast_val - actual_val))
    mpe = np.mean((forecast_val / actual_val)-1)
    rmse = np.sqrt(np.mean(np.square(forecast_val - actual_val)))
    corr = np.corrcoef(forecast_val, actual_val)[0,1]
    mins = np.amin(
        np.hstack((actual_val[:,None], 
                   forecast_val[:,None])),
        axis =1
        )
    maxs = np.amax(
        np.hstack((actual_val[:, None],
                   forecast_val[:,None])),
        axis = 1
        )
    minmax = 1- np.mean(mins/maxs)
    
    return({'MAPE': mape, 'ME': me,
            'MAE' : mae, 'MPE' : mpe,
            'RMSE' : rmse, 'CORR': corr,
            'minmax' : minmax})

df_forecst = forecast_df[:len(forecast_df)-1]
df_test = test_data[:len(test_data)-1]  
for act_col, frcst_col in zip(req_var_vec, forecast_df.columns):
    print(f"Forecast Accuracy of : {act_col}")
    accuracy_measures = forecast_accuracy_measures( 
        actual_val= df_test[act_col],
        forecast_val = df_forecst[frcst_col]
        )
    for mesrs_name, value in accuracy_measures.items():
        print(adjust_text(mesrs_name), ':', round(value, 3))
    print("--"*20)
    


                       
