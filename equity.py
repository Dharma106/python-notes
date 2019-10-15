# Stock price webscrapping
from __future__ import division
import requests
from bs4 import BeautifulSoup
import locale
import time
locale.setlocale(locale.LC_ALL, "")

#import pandas as pd
from pandas.io.json import json_normalize
import pandas as pd
pd.set_option('display.max_columns', None)
from nsepy import get_quote


def equity_output():
    
    """
    This function takes a dictionary format argument where key part takes equity
    name and value part takes moneycontrol corresponding equity url portion
    (just the category and its name definition). If not provided it selects the
    default equity as an example.
    
    dictionary should be in the form {"Shakti":"pumps/shaktipumpsindia/SPI08"}
    where key is "Shakti" and value is "pumps/shaktipumpsindia/SPI08"
    
    
    """
    
    page_address= "https://www.moneycontrol.com/india/stockpricequote/"
    stock_dict= {"Jet":"transport-logistics/jetairways/JA01",
                 "Spice Jet": "transport-logistics/spicejet/SJ01",
                 "Indigo" : "transport-logistics/interglobeaviation/IA04",
                 "Shakti":"pumps/shaktipumpsindia/SPI08",
                 "Rain":"cement-major/rainindustries/RC12",
                 "Apollo":"tyres/apollotyres/AT14",
                 "CDSL":"finance-investments/centraldepositoryservicesltd/CDS",
                 "Indian Overseas":"banks-public-sector/indianoverseasbank/IOB",
                 "Sintex Plastics":"plastics/sintexplasticstechnology/SPT",
                 "Sintex": "diversified/sintexindustries/SI27"}    
    
    Equity = []; Price = []; Volume = []; Close = []; Open = []
    ROC_Closing = []; ROC_Opening = []; 
    #    this is to print the time when the system has run checking the price
    
    run_timing = time.strftime('%I:%M %p')

    
    for i in range(len(stock_dict)):
        web_page = page_address + list(stock_dict.values())[i]
        page_sp = requests.get(web_page)
        page_sp_content = BeautifulSoup(page_sp.content, 'html.parser')
        equity_content= page_sp_content.find(id="content_nse")
        open_id = "n_open"      
        close_id = "n_prevclose"
        price_tick_type ="Nse_Prc_tick"        
        if(str(equity_content.find(class_ = "brdb PB5")) == 'None'):
             equity_content= page_sp_content.find(
                     class_ ="FL bseStDtl", id="content_bse")
             open_id = "b_open"
             close_id = "b_prevclose"
             price_tick_type ="Bse_Prc_tick"
        else :
             equity_content= page_sp_content.find(
                     class_ ="FR nseStDtl", id="content_nse")
             open_id = "n_open"      
             close_id = "n_prevclose"
             price_tick_type ="Nse_Prc_tick"
        req_equity_content= equity_content
        equity_price = req_equity_content.find(
                id=price_tick_type).find("strong").get_text()
        equity_price = float(equity_price)
        closing_price = req_equity_content.find(
                id=close_id, class_="gD_12 PB3").find("strong").get_text()
        closing_price = float(closing_price)
        open_price = req_equity_content.find(
                id = open_id, class_ = "gD_12 PB3").find(
                        "strong").get_text()
        open_price = float(open_price)
        traded_volumes= req_equity_content.find(
                class_="gD_12").find("strong").get_text()
        traded_volumes= locale.atoi(traded_volumes)
        Equity.append(list(stock_dict.keys())[i])
        Price.append(equity_price)
        Close.append(closing_price)
        Open.append(open_price)
        Volume.append(traded_volumes)
        ROC_Closing.append(str(format((Price[i]-Close[i]), '.2f') +
                               str(" (") + 
                               format((Price[i]/Close[i])-1,".2%") +
                               str(')')))
        ROC_Opening.append(str(format((Price[i]-Open[i]), '.2f') +
                               str(" (") + 
                               format((Price[i]/Open[i])-1,".2%") +
                               str(')'))) 
        
    equity_data = {'Equity': Equity,
                   'Close': Close,                   
                   'Current_Price': Price,
                   'Open' : Open,
                   'Volumes': Volume,
                   'ROC_Closing' : ROC_Closing,
                   'ROC_Opening' : ROC_Opening}
    equity_detail_table = pd.DataFrame(data = equity_data, 
                                       columns = ('Equity',
                                                  'Close',
                                                  'Current_Price',
                                                  'Open',                                                                                                    'ROC_Closing',
                                                  'ROC_Opening', 
                                                  'Volumes'))
#    print(run_timing)
    return run_timing, equity_detail_table
        


# get the live guote for equity
# get the live guote for equity
def live_quote(share_code = "indigo"):
    if type(share_code) != list:
        share_code = list(share_code.split())        
    share_code = [code.upper() for code in share_code]           
    req_columns = ['symbol','lastPrice', 'totalTradedVolume', 'open',
                   'dayHigh', 'dayLow', 'previousClose']
    rename_col = ['symbol', 'LTP', 'Vol', 'Open', 'High', 'Low', 'PrevClose']
    req_df = pd.DataFrame(columns=rename_col)
    for code in share_code:
        live_data =json_normalize(get_quote(code))
        temp_data = live_data[req_columns]
        temp_data.columns = rename_col
        req_df = req_df.append(temp_data)       
    return req_df

