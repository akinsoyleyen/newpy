from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://cma-cgm.com')
elem = browser.find_element_by_css_selector('#ContainerTracking_Reference')
elem2 = browser.find_element_by_css_selector('#track > div.c-hpforms--actions > div')
print(elem.text)
elem.send_keys('CGMU3948573')
elem.submit()