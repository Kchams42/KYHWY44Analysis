from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#options = webdriver.ChromeOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(options=options)

driver.get("http://crashinformationky.org/AdvancedSearch")
#select = Select(driver.find_element_by_class_name('eqjs-addrow eqjs-qp-addrow'))
#select.select_by_visible_text('County')
try: 
   element =  WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "eqjs-addrow eqjs-qp-addrow")))
   element.click()
except:
   driver.error_handler()


#link = driver.find_element_by_link_text("Add Property")
#link.click()eqjs-qp-condition-button eqjs-qp-condition-button-addPredicate