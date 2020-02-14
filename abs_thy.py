from selenium import webdriver
import time

#web sayfasi acilacak
#web sayfasindaki belirli noktaya awb nosu girilecek
#list dugmesine basilacak



awb_number = '36264642'
adress = 'https://www.turkishcargo.com.tr/en/online-services/shipment-tracking'
browser = webdriver.Chrome()
browser.get(adress)

awb_searchfield = browser.find_element_by_css_selector('#serviceform > div:nth-child(6) > div.col-md-4.col-sm-4.col-xs-8 > div > div > input')
time.sleep(3)
awb_filled_searchfield = awb_searchfield.send_keys(awb_number)

list_button = browser.find_element_by_css_selector('#serviceform > div:nth-child(8) > div:nth-child(2) > button')
list_button.click()
time.sleep(3)

last_movement = browser.find_element_by_css_selector('#accordion > li > div.submenu > div:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2)')
last_movement = last_movement.text

print(last_movement)

