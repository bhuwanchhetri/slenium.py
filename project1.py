from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s = Service("C:/Users/SARKAR/PycharmProjects/pythonProject1/Driver/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.demo.guru99.com/V4/index.php")
#print(driver.title)  #title of the page
#print(driver.current_url) #returns the url of page
#driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()  # remove double quote from xpath and put single quote
#driver.find_element_by_name("uid").send_keys("mngr379422")
#driver.find_element_by_name("password").send_keys("mAdydun")
#driver.find_element_by_name("btnLogin").click()
driver.find_element(By.NAME, "uid").send_keys("mngr379422")
driver.find_element(By.NAME, "password").send_keys("mAdydun")
driver.find_element(By.NAME, "btnLogin").click()
time.sleep(5)
driver.close() #it closes only the parent window
#driver.quit() #it closes all browser


#for fixing executable path depreceted we should pass service object in selenium python
