from zipfile import ZipFile
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
import glob
import pandas as pd
import os
import zipfile
import webbrowser
import matplotlib.pyplot as plt


 
#setting up the webdriver and url(*Stretch Goal-Using a webscraper*)
class WebScrape():
    global options
    options = Options() 
     

    def webdriver_setup():
        time.sleep(1)
    
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--enable-logging')
        options.add_experimental_option('detach', True)
     
    service = Service(ChromeDriverManager().install())
    global driver
    driver  = webdriver.Chrome(service=service, options=options)
    url = "http://crashinformationky.org/AdvancedSearch"   
    
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    
#filling  in the date range
    def date_input():
        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/a"))).click()
        time.sleep(1)
        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[10]/div/div[3]"))).click()
        time.sleep(1)
        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/a"))).click()
        time.sleep(1)
        field = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/input")
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys('01/01/2013')
        field.send_keys(Keys.ENTER)
        time.sleep(1)
        range = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/a')
        range.click()
        between = driver.find_element(By.XPATH, '/html/body/div[11]/div/div[9]')
        between.click()
        time.sleep(1)
        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/a"))).click()
        time.sleep(1)
        field = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[4]/input")
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys('12/31/2021')
        field.send_keys(Keys.ENTER)
        time.sleep(1)

#selecting the users county choice
    def add_county():
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

#adding in the roadway number
    def roadway():
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
        actions = ActionChains(driver)
        actions.send_keys(road)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(1)

#executing the search
def get_file():
    execute= driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div[1]/div[2]/div[2]')
    execute.click()
    time.sleep(35)

#selecting export method
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[2]/ul/li[3]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div/div[5]/div/input').click()

#exporting the file
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[3]/div/a').click()
    time.sleep(25)

#finding the file the was downloaded
    list_of_files= glob.glob(r"c:\Users\kcham\Downloads\*")
    latest_file = max(list_of_files, key=os.path.getmtime)

#extracting the incident file to a specific location
    with zipfile.ZipFile(latest_file, mode='r') as archive:
         archive.extract("Incident.txt", path ='d:projects')

#removing the zip file  
    os.remove(latest_file)

#converting the file into a data frame (*Cateory 2- reading data from an external file, Stretch goals- using pandas to perform data analysis)
def df_convert():
    global df
    df= pd.read_csv('d:projects/Incident.txt')
    os.remove('d:projects/Incident.txt')

#changing date format
    df['year'] =pd.DatetimeIndex(df['CollisionDate']).year

#selecting columns to use 
    useful_columns = [39,22,23,24,]
    df = df[df.columns[useful_columns]]

#chaning the data display
    df = df.groupby(['year']).sum()


#displaying data (*Category 3)
def display():
    with open('str.html', 'w') as f:
        df.to_html(f)
 
    filename = 'str.html'
    webbrowser.open_new_tab(filename)
    plt.figure
    df.plot.line()
    plt.show()

def main():
    time.sleep(1)
    print('This program will show crash data for specific roadways in specific counties in Kentucky.\n')
    global county 
    county = input('Please select a county from Kentucky\n')
    global road
    road = input('Please provide a valid road number in the county selected above. (ex: shelbyville road would be just 60)\n')
   
    webscrape = WebScrape
    webscrape.webdriver_setup()
    webscrape.date_input()
    webscrape.add_county()
    webscrape.roadway()
    get_file()
    df_convert()
    display()
    

if __name__ == "__main__":
    main()