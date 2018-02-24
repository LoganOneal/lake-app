import bs4 as bs
import urllib.request
import csv   
import datetime




source = urllib.request.urlopen('https://www.tva.gov/Environment/Lake-Levels/Cherokee').read()

soup = bs.BeautifulSoup(source,'lxml')

table = soup.findAll('table')[1]


x = (len(table.findAll('tr')) - 1)
for row in table.findAll('tr')[1:x]:
    col = row.findAll('td')
    level= col[2].getText()

currentDT = datetime.datetime.now()
time = currentDT.strftime("%Y/%m/%d")

data=[time,level]

with open(r'out.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(data)

print(level)
