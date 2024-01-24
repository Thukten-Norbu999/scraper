
##Module Imports
from selenium import webdriver
#from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


##Import Other modules
import time


##Import Functions
from data import data
from post import give
from scrapper import sci


index = []
liIpt = str(input('Enter the name of excel sheet with the index(example.xlsx):  '))
data(liIpt, index)


output = []

outS = str(input('Enter the name of output excel sheet with extension(example.xlsx):  '))

# stream = str(input('Choose the grade of which details is required\nGrade below 11\nGrade 11 Sci\nStream Sci\nStream Com\nStream Arts  ')).lower()



sci(index, output)


#Output
give(outS, output)

