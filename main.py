
##Module Imports
from selenium import webdriver
#from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


##Import Other modules
import time


##Import Functions
from data import data
from post import give



index = []
liIpt = str(input('Enter the name of excel sheet with the index(example.xlsx):  '))
data(liIpt, index)


output = []

outS = str(input('Enter the name of output excel sheet with extension(example.xlsx):  '))

for i in index[:153]:
    if i == None:
        pass
    else:
        PATH = 'C:\driver\chromedriver.exe'
        driver = webdriver.Chrome(PATH)
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
        name = driver.find_element(By.XPATH,"//*[@id='tt']/tr[1]/td[2]").text.title()
        # main sub #
        eng = float(driver.find_element(By.XPATH, '//*[@id="tbh"]/tr[2]/td[4]').text)
        dzo = float(driver.find_element(By.XPATH, '//*[@id="tbh"]/tr[3]/td[4]').text)
        math = driver.find_element(By.XPATH, '//*[@id="tbh"]/tr[4]/td[4]').text
        #Sci Sub #
        phy = float(driver.find_element(By.XPATH, '//*[@id="tbh"]/tr[6]/td[4]').text)
        chem = float(driver.find_element(By.XPATH, '//*[@id="tbh"]/tr[7]/td[4]').text)
        bio = driver.find_element(By.XPATH, '//*[@id="tbh"]/tr[8]/td[4]').text

        ict = float(driver.find_element(By.XPATH, "//*[@id='tbh']/tr[10]/td[4]").text)
        perc = float(driver.find_element(By.XPATH, "//*[@id='ftr']/tr/th[2]").text.split('Percentage:  ')[1][:-1])
        result = driver.find_element(By.XPATH, '//*[@id="ftr"]/tr/th[3]').text.split('Result:  ')[1]

        if math != 'NA' and bio != 'NA':
            math, bio = float(math), float(bio)
        elif math != 'NA' and bio == 'NA':
            math = float(math)
        else:
            bio = float(bio)
    
        #Ouput preparation
        print((i,name,eng, dzo, math, phy, chem, bio, ict, perc))
        output.append((i,name,eng, dzo, math, phy, chem, bio, ict, perc, result))
        
        driver.quit()


#Output
give(outS, output)

