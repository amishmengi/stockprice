import requests
from bs4 import BeautifulSoup
stock_url="https://www.google.com/search?sxsrf=ALeKk02y5zl-xjcHLi6uby23olMRQdAbJQ%3A1588711623576&ei=x9CxXoPkIvGY4-EPw4ud4Aw&q=tata+motors+share+price+nse&oq=tata+motors+share+price+nse&gs_lcp=CgZwc3ktYWIQAzIKCAAQgwEQRhD6ATICCAAyBQgAEIMBMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoECAAQR1DgO1iaQGCrSGgAcAJ4AIABsAGIAaMFkgEDMC40mAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwjD4-T_y53pAhVxzDgGHcNFB8wQ4dUDCAw&uact=5"
def checker() :
    response=requests.get(stock_url)
    ##print(response.text)
    soup=BeautifulSoup(response.content,'html.parser')
    data=soup.find("div", {"class":"BNeawe iBp4i AP7Wnd"}).get_text().split(" ")[0]
    print(data)
while True:
    checker()
