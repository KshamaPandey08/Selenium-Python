import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
#driver= webdriver.Chrome("C:\Software\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Chrome(ChromeDriverManager().install())
  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
driver.get("https://www.google.com/")
print('driver title:', driver.title)
print('driver name: ', driver.name)
print('driver url', driver.current_url)
# search= driver.find_element(By.ID,"")
# search.send_keys("testing")

driver.find_element(By.ID,'APjFqb').send_keys('hello')
driver.find_element(By.ID,'APjFqb').submit()


time.sleep(5)
