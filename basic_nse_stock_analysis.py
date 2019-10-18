#!/usr/bin/env python
# coding: utf-8

from nsetools import Nse
from nsepy import get_history, get_quote
from datetime import date
import pandas as pd
#use pandas package to create dataframe object from the json object
from pandas.io.json import json_normalize
import numpy as np
nse = Nse()

# to get the quotation infor of stocks 
nse.get_index_quote("nifty midcap 150")

# get all stocks codes and the company name traded on NSE
all_stock_codes = nse.get_stock_codes(cached=False)

# get the list of codes of all the traded indices with return type as list
index_codes = nse.get_index_list()
# pprint(index_codes)

"""
Advances Declines an important feature which, in a brief snapshot, tells the story of trading day for the given index.
It contains the numbers of rising stocks, falling stocks and unchanged stock in a given trading day, per index.
"""
adv_dec = nse.get_advances_declines()
#pprint(adv_dec)

top_gainers = nse.get_top_gainers()
df_top_gainers = pd.DataFrame(top_gainers)
req_columns = ["symbol", "openPrice", "highPrice", "lowPrice", "previousPrice", "tradedQuantity"]
df_top_gainers[req_columns]

top_losers = nse.get_top_losers()
df_top_losers = pd.DataFrame(top_losers)
df_top_losers[req_columns]

# get lot size of all stocks and index of future and options market
#nse.get_fno_lot_sizes()

#share_code = "indigo" 
#share_code.upper()
#start_date = date(2017,1,1)
#end_date = date(2019,8,26)
#share_code_hist_data = get_history(symbol=share_code, start=start_date, end= end_date)
#trading_date = pd.DataFrame({'d': share_code_hist_data.index}, index=share_code_hist_data.index)
#pd_trading_date = pd.to_datetime(trading_date.d)
#day_of_week = pd_trading_date.dt.weekday_name
#share_code_hist_data.insert(1, 'day_name', day_of_week)
#req_hist_columns = ['day_name','Symbol', 'Prev Close', 'Open', 'High', 'Low', 'Close', 'Volume']
share_code_hist_data= pd.read_csv('indigo_hist_data_2017.csv')
req_hist_columns = ['day_name','Symbol', 'Prev Close', 'Open', 'High', 'Low', 'Close', 'Volume']
start_date = date(2017,1,1)
end_date = date(2019,8,26)
req_data = share_code_hist_data.Date >= start_date  & share_code_hist_data.Date <= end_date
share_code_hist_data = share_code_hist_data.D

train_data = share_code_hist_data[req_hist_columns]
df1 = train_data.shift(periods=1)
df2 = train_data
tot_col = len(df2.columns)
df2.insert(tot_col,'open-close', df2.Open - df2.Close)
df2.insert(tot_col, 'close-low', df2.Close - df2.Low)
df2.insert(tot_col,'open-low', df2.Open - df2.Low)
df2.insert(tot_col, 'pc-open', df2['Prev Close'] - df2['Open'])

get_ipython().run_line_magic('matplotlib', 'inline')
df2['open-low'].plot(figsize=(15,5), legend=True)
df2['close-low'].plot(legend = True)
df2['pc-open'].plot(legend = True)
df2['open-close'].plot(legend =True)
#df2.open_vs_last.plot(secondary_y= True, legend=True)
day = ['Friday', "Monday"]
filter_day = df2.day_name.isin(day)
df2[filter_day]

df2[filter_day].describe()

value  = 13
open_minus_low =  df2['open-low'] > value
close_minus_low = df2['close-low'] > value
avg_val_oml = df2['open-low'].mean()
avg_val_cml = df2['close-low'].mean()
print({'open_minus_low > %.f is %.f times out of %.0f' %(value, open_minus_low.sum(), open_minus_low.count())})
print({'close_minus_low > %.f is %.f times out of %.0f' %(value, close_minus_low.sum(), close_minus_low.count())})
print('The average value corresponding to open-minus-low is %.f and for close-minus-low is %.f' %(avg_val_oml, avg_val_cml))

open_eqls_low = df2.Open == df2.Low
close_eqls_low = df2.Close == df2.Low
print({"open_eqls_low" : open_eqls_low.sum(), "close_eqls_low": close_eqls_low.sum()})
print(df2[open_eqls_low])
pc_open = df2['pc-open'] <0
print(df2[pc_open]['open-low'].mean())
print(df2[pc_open]['close-low'].mean())

share_code = "indigo" 
share_code.upper
req_columns = ['symbol','series', 'previousClose', 'open', 'dayHigh', 'dayLow', 'closePrice', 'lastPrice', 'totalTradedVolume']
live_data =json_normalize(nse.get_quote(share_code))
req_df = live_data[req_columns]
req_df

{'open-low' : req_df.open-req_df.dayLow, 'close-low':req_df.closePrice- req_df.dayLow}

