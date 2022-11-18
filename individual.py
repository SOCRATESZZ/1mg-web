from bs4 import BeautifulSoup
import requests

import xlwt
from xlwt import Workbook

wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0,0, 'name')
sheet1.write(0,1, 'Prescription')
sheet1.write(0,2, 'Company')
sheet1.write(0,3, 'contents')

x = 1
y = 0

header = {'Origin': 'https://www.1mg.com',
'Referer': 'https://www.1mg.com/drugs-all-medicines?label=a',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

html_text = requests.get(  url="https://www.1mg.com/drugs-all-medicines?label=a",headers=header).text

soup = BeautifulSoup(html_text,'lxml')

meds = soup.find_all('div', {'class':'style__flex-1___A_qoj'})

allData = []

url = "https://www.1mg.com/drugs-all-medicines?page=1&label=a"

page = 1

while page <= 65:
    url = "https://www.1mg.com/drugs-all-medicines?page={p}&label=x".format(p=page)
    html_text = requests.get(url=url, headers=header).text
    soup = BeautifulSoup(html_text, 'lxml')
    meds = soup.find_all('div', {'class': 'style__flex-1___A_qoj'})

    for name in meds:
        # print("----------")
        obj = []
        c = 0
        for i in name:
            if(c==2) :
                i = i.find_all('div')[1]
                # print(i.text)
            if(c==0):
                i = i.find_all('div')[0]
                # print(i.text)
            # else:
            obj.append(i.text)
            c+=1
        sheet1.write(x,0,obj[0])
        sheet1.write(x, 1, obj[1])
        sheet1.write(x, 2, obj[2])
        sheet1.write(x, 3, obj[3])
        x+=1
        allData.append(obj)
        # print(name.div.text)

        # for i in name:
        #     print(i)
    page+=1
    print(page)
wb.save('Xdatabase.xls')
print('successful')
# print(allData)