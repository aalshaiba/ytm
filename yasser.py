from bs4 import BeautifulSoup
import requests
import xlwt

url = 'https://www.google.com'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

wb = xlwt.Workbook()
ws = wb.add_sheet('Test Sheet')

ws.write(0, 0, soup.title.text)

wb.save('test.xls')