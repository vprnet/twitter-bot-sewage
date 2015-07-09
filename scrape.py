import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'https://anrweb.vt.gov/DEC/WWInventory/SewageOverflows.aspx'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class': 'dataList'})

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./sewage.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Index", "Start Date", "End Date", "Start/End Times", "Municipality", "Location", "Waterbody", "Description of Incident", "Estimated Volume (gallons)", "Wastewater Treatment Facility", "Contact Person"])
list = writer.writerows(list_of_rows)
