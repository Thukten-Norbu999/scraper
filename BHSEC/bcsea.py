from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time


INDEX = input('index no: ')
DOB = input('DOB in mm/dd/yy: ')

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://class12result.cloud/result2021')

index = driver.find_element(By.XPATH, "//*[@id='indexno']")
index.send_keys(INDEX)
index.send_keys(Keys.RETURN)

dob = driver.find_element(By.XPATH, "//*[@id='dob']")
#dob.clear()
dob.send_keys(DOB)
dob.send_keys(Keys.RETURN)

eng = float(driver.find_element(By.XPATH, '//*[@id="myTable"]/tbody/tr[4]/th[2]').text)
dzo = float(driver.find_element(By.XPATH, '//*[@id="myTable"]/tbody/tr[5]/th[2]').text)
            
math = float(driver.find_element(By.XPATH, '//*[@id="myTable"]/tbody/tr[6]/th[2]').text)
                #Sci Sub #
phy = float(driver.find_element(By.XPATH, '//*[@id="myTable"]/tbody/tr[7]/th[2]').text)
chem = float(driver.find_element(By.XPATH, '//*[@id="myTable"]/tbody/tr[8]/th[2]').text)
bio = float(driver.find_element(By.XPATH, '//*[@id="myTable"]/tbody/tr[9]/th[2]').text)

marks = [eng, dzo, math, phy, chem, bio]
c_Math, c_Bio = driver.find_element(By.XPATH, '//*[@id="myTable"]/tbody/tr[6]/th[1]').text, driver.find_element(By.XPATH, '//*[@id="myTable"]/tbody/tr[9]/th[1]').text

time.sleep(20)

driver.quit()
print(c_Math,c_Bio)

print(marks)