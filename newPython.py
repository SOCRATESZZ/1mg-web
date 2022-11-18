from bs4 import BeautifulSoup
import requests

header = {'Origin': 'https://www.1mg.com',
'Referer': 'https://www.1mg.com/drugs-all-medicines?label=a',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

html_text = requests.get(  url="https://www.1mg.com/drugs-all-medicines?label=a",headers=header).text

soup = BeautifulSoup(html_text,'lxml')

meds = soup.find('div', {'class': 'style__flex-1___A_qoj'})

obj_name = []
for med in meds:
    for name in med:
        # print(name.find_all('div'))
        obj_name.append(name.find_all('div'))
# print(obj_name)
    print(obj_name[0][0].text, " ", obj_name[2][1].text, " ", obj_name[3][0].text)

# for pt in obj_name:
#     print(pt)
# print(obj_name[3][0].text)
    # print(obj[0][0].text,obj[2][1].text)

