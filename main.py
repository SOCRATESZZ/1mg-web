from bs4 import BeautifulSoup
import requests

header = {'Origin': 'https://www.1mg.com',
'Referer': 'https://www.1mg.com/drugs-all-medicines?label=a',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

html_text = requests.get(  url="https://www.1mg.com/drugs-all-medicines?label=a",headers=header).text

soup = BeautifulSoup(html_text,'lxml')
meads = soup.find_all('div', {'class':'style__font-bold___1k9Dl style__font-14px___YZZrf style__flex-row___2AKyf style__space-between___2mbvn style__padding-bottom-5px___2NrDR'})
company = soup.find_all('div',{'class':'style__padding-bottom-5px___2NrDR'})

for name in meads:
    obj = name.find_all('div')
    print(obj[0].text, obj[1].text)


# mead_name = meads.find('div')

# print(mead_name)
