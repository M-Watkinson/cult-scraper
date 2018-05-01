from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

html = urlopen("https://en.wikipedia.org/wiki/List_of_new_religious_movements")
bsObj = BeautifulSoup(html, "html.parser")
cultList = bsObj.findAll("tr")
#for cult in cultList:
    #print(cult.get_text())
with open('cultlistings.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for cult in cultList:
        writer.writerow(cult.get_text())
csvfile.close()
