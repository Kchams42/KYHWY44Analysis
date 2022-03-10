from select import select
from shutil import move
from typing import List
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.chrome.service import Service

s = Service( "D:\chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.get("http://crashinformationky.org/AdvancedSearch")

driver.maximize_window()

add_property= driver.find_element(By.XPATH, '//*[@id="QueryPanel"]/div[3]/a')
add_property.click()
county_name = driver.find_element(By.XPATH, '//*[@id="QueryPanel-EntitiesMenu"]/div/div[4]')
county_name.click()
driver.implicitly_wait(32)
county_name_select = driver.find_element(By.XPATH, '//*[@id="QueryPanel-cond-1"]/div[3]/a')
county_name_select.click()
driver.implicitly_wait(132)
county_input = driver.find_element(By.ID, 'searchBox')
county_input.send_keys('jefferson')
driver.implicitly_wait(32)
county_final = driver.find_element(By.CSS_SELECTOR, '#QueryPanel-cond-1-EditorMenu > div.eqjs-menu-scrollDiv > div')
driver.implicitly_wait(32)
county_final.click()
driver.implicitly_wait(30)
add_property= driver.find_element(By.XPATH, '//*[@id="QueryPanel"]/div[3]/a')
add_property.click()
collision_date = driver.find_element(By.XPATH, '//*[@id="QueryPanel-EntitiesMenu"]/div/div[3]')
collision_date.click()
driver.implicitly_wait(32)
range = driver.find_element(By.XPATH, '//*[@id="QueryPanel-cond-2"]/div[2]/a')
range.click()
between = driver.find_element(By.XPATH, '//*[@id="QueryPanel-cond-2-OperatorsMenu"]/div/div[9]')
between.click()
driver.implicitly_wait(400)
#date_one = driver.find_element(By.CSS_SELECTOR, '#QueryPanel-cond-2 > div:nth-child(4)')
#date_one.click()