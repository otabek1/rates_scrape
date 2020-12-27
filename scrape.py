import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

banks = [
    {
        "name":"O'zbekiston Respublikasi Markaziy Banki",
        "rate": "",
        "buy":""
    },
    {
        "name":"Milliy Bank",
        "buy":"",
        "sell":""
    },
    {
        "name":"Hamkorbank",
        "buy":"",
        "sell":""
    },
    {
        "name":"Asakabank",
        "buy":"",
        "sell":""
    },
    {
        "name":"Infinbank",
        "buy":"",
        "sell":""
    },
    {
        "name":"Agrobank",
        "buy":"",
        "sell":""
    },
    {
        "name":"Mikrokreditbank",
        "buy":"",
        "sell":"",
    },
    {
        "name":"Xalq Banki",
        "buy":"",
        "sell":""
    },
    {
        "name":"Orient Finans Bank",
        "buy":"",
        "sell":""
    },
    {
        "name":"Trast Bank",
        "buy":"",
        "sell":""
    },
     {
        "name":"Kapitalbank",
        "buy":"",
        "sell":""
    },

]
def cbu_rate():
    cbu_rate_req = requests.get("https://nbu.uz/uz/exchange-rates/")
    cbu_soup = BeautifulSoup(cbu_rate_req.text,"html.parser")
    cbu_rate_num = cbu_soup.select('.kursdata table td')[1].getText()
    banks[0]["rate"] = cbu_rate_num

def nbu_rate():
    nbu_rate_req = requests.get("https://nbu.uz/uz/exchange-rates/")
    nbu_soup = BeautifulSoup(nbu_rate_req.text,"html.parser").select('.kursdata table td')
    nbu_buy = nbu_soup[2].getText()[:-3]
    nbu_sell = nbu_soup[3].getText()[:-3]
    banks[1]["buy"] = nbu_buy
    banks[1]["sell"] = nbu_sell

def hamkorbank_rate():
    hk_rate_req = requests.get("https://hamkorbank.uz/uz/exchange-rate/")
    hk_soup = BeautifulSoup(hk_rate_req.text,"html.parser").select(".exchangeRates__content--wraps-content .list .body li")
    hk_buy = hk_soup[3].getText()
    hk_sell = hk_soup[4].getText()
    banks[2]["buy"] = hk_buy
    banks[2]["sell"] = hk_sell

def asaka_rate():
    asaka_req = requests.get("https://new.asakabank.uz/uz")
    asaka_soup = BeautifulSoup(asaka_req.text,"html.parser").select("td[data-currency=USD]")
    asaka_buy = asaka_soup[0].getText().replace(",","").replace(" ","")[:-2]
    asaka_sell = asaka_soup[1].getText().replace(",","").replace(" ","")[:-2]
    banks[3]["buy"] = asaka_buy
    banks[3]["sell"] = asaka_sell

def infin_rate():
    infin_req = requests.get("https://www.infinbank.com/uz/")
    infin_soup = BeautifulSoup(infin_req.text,"html.parser").select(".currency-table td")
    infin_buy = infin_soup[1].getText()[:-3]
    infin_sell = infin_soup[7].getText()[:-3]
    banks[4]["buy"] = infin_buy
    banks[4]["sell"] = infin_sell

def agro_rate():
    agro_req = requests.get("https://agrobank.uz/uz/exchange_rates")
    agro_soup = BeautifulSoup(agro_req.text,"html.parser").select("tr")[1].select("td")
    agro_buy = agro_soup[3].getText()[:-3].replace(" ","")
    agro_sell = agro_soup[2].getText()[:-3].replace(" ","")
    banks[5]["buy"] = agro_buy
    banks[5]["sell"] = agro_sell

def mikro_rate():
    mikro_req = requests.get("https://mikrokreditbank.uz/")
    mikro_soup = BeautifulSoup(mikro_req.text,"html.parser").select(".convertor-content table tr td")
    mikro_buy = mikro_soup[1].getText()[:-3]
    mikro_sell = mikro_soup[2].getText()[:-3]
    banks[6]["buy"]=mikro_buy
    banks[6]["sell"]=mikro_sell

def xalq_rate():
    xalq_req = requests.get("https://www.xb.uz/", verify=False)
    xalq_soap_buy = BeautifulSoup(xalq_req.text,"html.parser").select(".inner__rate")
    xalq_soap_sell = BeautifulSoup(xalq_req.text,"html.parser").select(".buying__rate")
    xalq_buy = xalq_soap_buy[1].getText()[:-4].replace(" ","")
    xalq_sell = xalq_soap_sell[1].getText()[:-4].replace(" ","")
    banks[7]["buy"] = xalq_buy
    banks[7]["sell"] = xalq_sell

def orient_rate():
    orient_req = requests.get("https://ofb.uz/uz/about/kurs-obmena-valyut/")
    orient_soup = BeautifulSoup(orient_req.text,"html.parser").select("body table td")
    orient_buy = orient_soup[2].getText().strip()[:-3]
    orient_sell = orient_soup[3].getText().strip()[:-3]
    banks[8]["buy"] = orient_buy
    banks[8]["sell"] = orient_sell

def trust_rate():
    trust_req = requests.get("https://trustbank.uz/uz/")
    trust_soap = BeautifulSoup(trust_req.text,"html.parser").select(".rate__currency_value")
    trust_buy = trust_soap[0].select("span")[0].getText()
    trust_sell = trust_soap[1].select("span")[0].getText()
    banks[9]["sell"] = trust_sell
    banks[9]["buy"] = trust_buy

def kapital_rate():
    kapital_req = requests.get("https://kapitalbank.uz/uz/welcome.php")
    kapital_soup = BeautifulSoup(kapital_req.text,"html.parser").select(".item-rate span")
    kapital_buy = kapital_soup[0].getText()
    kapital_sell = kapital_soup[2].getText()
    banks[10]["buy"] = kapital_buy
    banks[10]["sell"] = kapital_sell

cbu_rate()
nbu_rate()
hamkorbank_rate()
asaka_rate()
infin_rate()
agro_rate()
mikro_rate()
xalq_rate()
orient_rate()
trust_rate()
kapital_rate()
new_banks = sorted(banks, key = lambda k:k['buy'], reverse=True)
# # # print(banks)
print(new_banks)

