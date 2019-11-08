from bs4 import BeautifulSoup
import requests
import xlwt
from lxml import html


url = 'https://mail.google.com/'

response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')

tree = html.fromstring(response.text)

print(tree.xpath("//title/text()")[0])

# wb = xlwt.Workbook()
# ws = wb.add_sheet('Test Sheet')
#
# ws.write(0, 0, soup.title.text)
#
# wb.save('test.xls')