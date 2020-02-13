from selenium import webdriver
import time
import openpyxl
import os

#!HAPAGLLOYD CLASS

os.chdir('/Users/akin/onedrive/python3/documents')
workbook = openpyxl.load_workbook('konteynerler.xlsx')
sheet = workbook.get_sheet_by_name('Sheet1')
cell = sheet['A1']


class hapagContainerTracking:

    def __init__(self, shippingLine, containerNumber):
        
        print('Now looking for' + ' ' + containerNumber)

        self.shippingLine = shippingLine
        self.containerNumber = containerNumber

        global hapagContainerType
        global hapagLastMovement
        
        #browser ac
        browser = webdriver.Chrome()
        browser.get(shippingLine)
        time.sleep(3)
        # Arama alaninin bulunmasi
        searchField = browser.find_element_by_css_selector('#tracingvalue')
        time.sleep(7)

        # Arama alanina konteyner numarasinin yazilmasi
        searchFieldFilled = searchField.send_keys(containerNumber)

        # Trace Button basma
        hapagButton = browser.find_element_by_css_selector(
            'body > div.hal-page.hal-page--home.page-home > div.hal-page-body > div.hal-stagehome > div:nth-child(3) > div > div > div:nth-child(1) > div > button > span')
        hapagButton.click()

        # 5sn bekleme
        time.sleep(5)

        # Container Type olan alanin bulunmasi
        hapagContainerType = browser.find_element_by_css_selector(
            '#tracing_by_container_f\:hl29 > tbody > tr > td > div > table > tbody > tr > td:nth-child(3) > table > tbody > tr > td.inputNonEdit > span')
        hapagLastMovement = browser.find_element_by_css_selector(
            '#tracing_by_container_f\:hl56 > tbody > tr > td > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr > td.inputNonEdit > span')

        # Container tipi nedir?
        hapagContainerType = hapagContainerType.text
        hapagLastMovement = hapagLastMovement.text

        print('The Type of the Container is:' + hapagContainerType)
        print(hapagLastMovement)
        
        #WRITE THE ANSWER FROM HAPAGLLOYD TO A FILE!
        containerStatusFile = open("Containers.txt", "a")
        containerStatusFile.write(containerNumber + " " + hapagLastMovement + "\n")
        containerStatusFile.close()



# Hangi shipping line kontrol edilecek?
shippingLine = input('What is the shipping line?').lower()

#!THE IF STATEMENT PART OF THE PROGRAM

if shippingLine == "hapaglloyd":

    shippingLine = 'https://www.hapag-lloyd.com/en/home.html'

    print("OK....Passing to the relative class")

    for i in range(2, 7):
        cell_value = sheet.cell(row=i, column=1).value
        hapagContainerTracking(shippingLine, cell_value)
else:
    print('We only support HapagLloyd for now!')





