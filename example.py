'''
importing selenium along with some of its functions
to make it easier
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time

i = str(input('Enter Your Index Correctly:  '))


PATH = 'C:\chromedriver-win64\chromedriver.exe'
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://www.aeresult.yhss.edu.bt/')


#Dropdown Selector
dropdown = driver.find_element(By.ID, 'section')
select = Select(dropdown)
select.select_by_index(2)

    #Input Index
textfield = driver.find_element(By.XPATH, "/html/body/div/section/div[2]/div[4]/div/div/div/form/input")
textfield.send_keys(i)
textfield.send_keys(Keys.RETURN)
    
    #Scrape
'''
    here we get the elements according to the XPATH(which is like a file directory but in html)
'''
name = driver.find_element(By.XPATH,"//*[@id='tt']/tr[1]/td[2]").text.title()
eng = float(driver.find_element(By.XPATH, '//*[@id="tbh"]/tr[2]/td[4]').text)
dzo = float(driver.find_element(By.XPATH, '//*[@id="tbh"]/tr[3]/td[4]').text)
math = float(driver.find_element(By.XPATH, '//*[@id="tbh"]/tr[4]/td[4]').text)
phy = float(driver.find_element(By.XPATH, '//*[@id="tbh"]/tr[6]/td[4]').text)
chem = float(driver.find_element(By.XPATH, '//*[@id="tbh"]/tr[7]/td[4]').text)
bio = float(driver.find_element(By.XPATH, '//*[@id="tbh"]/tr[8]/td[4]').text)
ict = float(driver.find_element(By.XPATH, "//*[@id='tbh']/tr[10]/td[4]").text)
perc = float(driver.find_element(By.XPATH, "//*[@id='ftr']/tr/th[2]").text.split('Percentage:  ')[1][:-1])
result = driver.find_element(By.XPATH, '//*[@id="ftr"]/tr/th[3]').text.split('Result:  ')[1]

    #Ouput preparation
print((i,name,eng, dzo, math, phy, chem, bio, ict, perc, result))

time.sleep(15)

driver.quit()

