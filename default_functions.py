from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import getpass

#Collects the username of the person running the script to allow the driver path to work
Name = getpass.getuser()

#Sets the path to the chromedriver 
driver = webdriver.Chrome(r'/Users/'+Name+'/Documents/Python_Static/Drivers/chromedriver')

#The amount of time selenium will wait for the element to appear before throwing an exception
waitTime = 10

#Waits for, and clicks element specified by either Xpath, Id, or Name
class click:
    def Xpath(link):
        try:
            WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located((By.XPATH, link)))
            driver.find_element_by_xpath(link).click()
        except:
            input('COULD NOT FIND "'+str(link)+'" PLEASE ENTER MANUALLY AND PRESS ENTER TO CONTINUE')  

    def Id(link):
        try:
            WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located((By.ID, link)))
            driver.find_element_by_id(link).click()
        except:
            input('COULD NOT FIND "'+str(link)+'" PLEASE ENTER MANUALLY AND PRESS ENTER TO CONTINUE')  
    
    def Name(link):
        try:
            WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located((By.NAME, link)))
            driver.find_element_by_name(link).click()
        except:
            input('COULD NOT FIND "'+str(link)+'" PLEASE ENTER MANUALLY AND PRESS ENTER TO CONTINUE')  

#Waits for, and fills element specified by either Xpath, Id, or Name
class fill:
    def Xpath(fill,text):
        try:
            WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located((By.XPATH, fill)))
            driver.find_element_by_xpath(fill).clear()
            driver.find_element_by_xpath(fill).send_keys(text)
        except:
            input('COULD NOT FIND THE INPUT ASSOCIATED WITH "'+str(fill)+'" PLEASE ENTER MANUALLY AND PRESS ENTER TO CONTINUE') 

    def Id(fill,text):
        try:
            WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located((By.ID, fill)))
            driver.find_element_by_id(fill).clear()
            driver.execute_script(r'document.getElementById("'+fill+'").value="'+text+'"')
        except:
            input('COULD NOT FIND THE INPUT ASSOCIATED WITH "'+str(fill)+'" PLEASE ENTER MANUALLY AND PRESS ENTER TO CONTINUE') 

    def Name(fill,text):
        try:
            WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located((By.NAME, fill)))
            driver.find_element_by_name(fill).clear()
            driver.execute_script(r'document.getElementsByName("'+fill+'")[0].value="'+text+'"')
        except:
            input('COULD NOT FIND THE INPUT ASSOCIATED WITH "'+str(fill)+'" PLEASE ENTER MANUALLY AND PRESS ENTER TO CONTINUE') 

#Waits for, and clicks elements in a dropdown list. The element is selected by the dropdown attribute and then the element attribute that the user is looking for
class dropdown:
    def Nametext(name,value):
        try:
            WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located((By.NAME, name)))
            selection = Select(driver.find_element_by_name(name))
            selection.select_by_visible_text(value)
        except:
            input('COULD NOT FIND "'+str(value)+'" PLEASE ENTER MANUALLY AND PRESS ENTER TO CONTINUE')
    
    def Namevalue(name,value):
        try:
            WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located((By.NAME, name)))
            selection = Select(driver.find_element_by_name(name))
            selection.select_by_value(value)
        except:
            input('COULD NOT FIND "'+str(value)+'" PLEASE ENTER MANUALLY AND PRESS ENTER TO CONTINUE')

    def Idtext(ids,value):
        try:
            WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located((By.ID, ids)))
            selection = Select(driver.find_element_by_id(ids))
            selection.select_by_visible_text(value)
        except:
            input('COULD NOT FIND "'+str(value)+'" PLEASE ENTER MANUALLY AND PRESS ENTER TO CONTINUE')

    def Idvalue(ids,value):
        try:
            WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located((By.ID, ids)))
            selection = Select(driver.find_element_by_id(ids))
            selection.select_by_value(value)
        except:
            input('COULD NOT FIND "'+str(value)+'" PLEASE ENTER MANUALLY AND PRESS ENTER TO CONTINUE')

#Used to wait for elements to appear, but does not actually perform any actions
class wait:
    def Short(link):
        try:
            WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located((By.XPATH, link)))
        except:
            input('COULD NOT FIND "'+str(link)+'"') 
    
    def Long(link):
        try:
            WebDriverWait(driver, 20000).until(EC.visibility_of_element_located((By.XPATH, link)))
        except:
            input('COULD NOT FIND "'+str(link)+'"') 

#Used to get attributes from web elements
class get:
    def Text(link):
        WebDriverWait(driver, waitTime).until(EC.visibility_of_element_located((By.XPATH, link)))
        return driver.find_element_by_xpath(link).text

#Used to create new tabs and move between them
class tab:
    def New(link,num):
        driver.execute_script("window.open('"+link+"');")
        driver.switch_to.window(driver.window_handles[num])
    
    def Switch(number):
        window = driver.window_handles[number]
        driver.switch_to_window(window)