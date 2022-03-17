from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

county = input('Please select a county from Kentucky')
print(county)
road = input('Please provide the road number')
print(road)
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-extensions')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--enable-logging')
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
url = "http://crashinformationky.org/AdvancedSearch"



driver.get(url)
time.sleep(1)


WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/a"))).click()
time.sleep(1)
WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[10]/div/div[3]"))).click()
time.sleep(1)
WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/a"))).click()
time.sleep(1)
field = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/input")
field.send_keys(Keys.CONTROL + "a")
field.send_keys(Keys.DELETE)
field.send_keys('01/01/2016')
field.send_keys(Keys.ENTER)
time.sleep(1)
range = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/a')
range.click()
between = driver.find_element(By.XPATH, '/html/body/div[11]/div/div[9]')
between.click()
time.sleep(1)
add_property= driver.find_element(By.XPATH, '//*[@id="QueryPanel"]/div[3]/a')
add_property.click()
county_name = driver.find_element(By.XPATH, '//*[@id="QueryPanel-EntitiesMenu"]/div/div[4]')
county_name.click()
time.sleep(1)
county_name_select = driver.find_element(By.PARTIAL_LINK_TEXT, 'select')
county_name_select.click()
time.sleep(1)
county_input = driver.find_element(By.ID, 'searchBox')
county_input.send_keys(county)
time.sleep(1)
county_final = driver.find_element(By.XPATH, '//*[@id="QueryPanel-cond-2-EditorMenu"]/div[2]/div')
time.sleep(1)
county_final.click()
add_property= driver.find_element(By.XPATH, '//*[@id="QueryPanel"]/div[3]/a')
add_property.click()
time.sleep(1)
roadway_property = driver.find_element(By.XPATH, '//*[@id="QueryPanel-EntitiesMenu"]/div/div[10]')
roadway_property.click()
time.sleep(1)
starts_with = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[2]/a')
starts_with.click()
time.sleep(1)
contains =  driver.find_element(By.XPATH, '/html/body/div[11]/div/div[2]')
contains.click()
time.sleep(1)
enter_value = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[3]/a')
enter_value.click()
time.sleep(1)
#roadway_choice = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[2]/div[2]/div')
actions = ActionChains(driver)
actions.send_keys(road)
actions.send_keys(Keys.ENTER)
actions.perform()
time.sleep(1)
execute= driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[1]/div[2]/div[2]')
execute.click()
