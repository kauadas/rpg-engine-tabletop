import requests

from lxml import etree

from bs4 import BeautifulSoup

def loadSheet(url):

    with open(url) as data:
        html = data.read()
    
    soup = BeautifulSoup(html,'html.parser')
    

    atributes = soup.find_all('div' ,class_ = "ddbc-saving-throws-summary__ability ddbc-saving-throws-summary__ability--str")
    
    for i in atributes:
        print(i.text + "\n")
    

loadSheet("Gottes Zorn's Character Sheet - D&D Beyond.html")