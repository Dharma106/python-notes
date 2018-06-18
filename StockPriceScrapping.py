import requests
from bs4 import BeautifulSoup
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

page_sp = requests.get("https://www.moneycontrol.com/india/stockpricequote/pumps/shaktipumpsindia/SPI08")
page_sp_content = BeautifulSoup(page_sp.content, 'html.parser')
sp_nse_content= page_sp_content.find(id="content_nse")
sp_nse_price= sp_nse_content.find(class_="PA2").find("strong").get_text()
sp_nse_price = float(sp_nse_price)
sp_nse_volumes= sp_nse_content.find(class_="gD_12").find("strong").get_text()
sp_nse_volumes= locale.atoi(sp_nse_volumes)
