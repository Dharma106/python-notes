# Stock price webscrapping
import requests
from bs4 import BeautifulSoup
import locale
locale.setlocale(locale.LC_ALL, "")
import pandas as pd

def nse_equity_output():
    page_address= "https://www.moneycontrol.com/india/stockpricequote/"
    stock_dict= {"Jet":"transport-logistics/jetairways/JA01", 
                 "Shakti":"pumps/shaktipumpsindia/SPI08",
                 "Rain":"cement-major/rainindustries/RC12",
                 "Apollo":"tyres/apollotyres/AT14",
                 "CDSL":"finance-investments/centraldepositoryservicesltd/CDS",
                 "Indian Overseas":"banks-public-sector/indianoverseasbank/IOB",
                 "Sintex Plastics":"plastics/sintexplasticstechnology/SPT"}    
    equity_name = []
    price = []
    volume =[]
    
    for i in range(len(stock_dict)):
        web_page = page_address + stock_dict.values()[i]
        page_sp = requests.get(web_page)
        page_sp_content = BeautifulSoup(page_sp.content, 'html.parser')
        sp_nse_content= page_sp_content.find(id="content_nse")
        sp_nse_price= sp_nse_content.find(class_="PA2").find("strong").get_text()
        sp_nse_price = float(sp_nse_price)
        sp_nse_volumes= sp_nse_content.find(class_="gD_12").find("strong").get_text()
        sp_nse_volumes= locale.atoi(sp_nse_volumes)
        equity_name.append(stock_dict.keys()[i])
        price.append(sp_nse_price)
        volume.append(sp_nse_volumes)
        
    equity_data = {'Equity Name': equity_name,
               'Price': price,
               'Volumes': volume}
    equity_detail_table = pd.DataFrame(data = equity_data)
    print(equity_detail_table)        
