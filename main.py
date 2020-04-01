import requests
from bs4 import BeautifulSoup

EURO_RUB = 'https://www.google.com/search?client=ubuntu&channel=fs&q=euro+to+russian+ruble+exchange+rate&ie=utf-8&oe=utf-8'
DOLLAR_RUB = 'https://www.google.com/search?client=ubuntu&channel=fs&q=dollar+to+russian+ruble+exchange+rate&ie=utf-8&oe=utf-8'

DOLLAR_BYR = 'https://www.google.com/search?client=ubuntu&channel=fs&q=dollar+to+belarusian+ruble+exchange+rate&ie=utf-8&oe=utf-8'
EURO_BYR = 'https://www.google.com/search?client=ubuntu&channel=fs&q=euro+to+belarusian+ruble+exchange+rate&ie=utf-8&oe=utf-8'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'}

def getCurrencyRate(currency):
    full_page = requests.get(currency, headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "BNeawe iBp4i AP7Wnd"})
    currrency_text = convert[0].text
    currency_str = str.split(currrency_text, " ")
    currrency_float = float(currency_str[0])
    #f = open("output.html", "w")
    #f.write(full_page.content.decode("utf-8"))
    #f.close()
    return currrency_float

message = 'currency exchanges are:'

message += '\neuro to rub  \t' + str(getCurrencyRate(EURO_RUB))
message += '\ndollar to rub\t' + str(getCurrencyRate(DOLLAR_RUB))
message += '\neuro to byr  \t' + str(getCurrencyRate(EURO_BYR))
message += '\ndollar to byr\t' + str(getCurrencyRate(DOLLAR_BYR))

print(message)
