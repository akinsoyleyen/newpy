import bs4
import requests

#def getHapagEta(containerURL):
#    res = requests.get(containerURL) #Request modulu ile URL yi talep et ve bunu res variable da sakla
#    res.raise_for_status() #Herhangi bir hata var mi diye kontrol et

#    soup = bs4.BeautifulSoup(res.text, 'html.parser') #BeautifulSoup ile bu URL den alip res te sakladigimiz datayi text e donustur.
#    elems = soup.select('#tracing_by_container_f\:hl29 > tbody > tr > td > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr > td.inputNonEdit > span')
#    return elems[0].text.strip()

#containerType = getHapagEta('https://www.hapag-lloyd.com/en/online-business/tracing/tracing-by-container.html?container=HLBU9368791')
#print('The type of this container is'+ containerType)

res = requests.get('https://www.hapag-lloyd.com/en/online-business/tracing/tracing-by-container.html?container=HLBU9368791')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('#page-content > article > div > div > div > div.col-md-9 > div.page-content.clearfix > p:nth-child(17)')
print(elems)