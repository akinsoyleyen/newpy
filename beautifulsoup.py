import requests
import bs4


def getAmazonPrice(productUrl):
    res = requests.get(productUrl) #This will download the HTML
    res.raise_for_status() #Incase there is an error like 404 or 503 ; the program will crash here
    soup = bs4.BeautifulSoup(res.text, 'html.parser') #This will get all the HTML
    elems = soup.select('#kurlarContainer > table:nth-child(5) > tbody > tr:nth-child(1) > td:nth-child(4)')

price = getAmazonPrice('https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+page+site+area/bugun')
print(price)
