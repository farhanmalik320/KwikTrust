import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)

# get google.com
current_url = driver.get("https://develop-v2.d2ld8gf66npudc.amplifyapp.com/#/auth/login")
driver.maximize_window()

time.sleep(2)

#enter email
email_field=driver.find_element(By.XPATH,'//body/app-root[1]/app-full-layout[1]/div[1]/main[1]/app-login[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[1]').send_keys('testautomationsignatory@yopmail.com')

time.sleep(2)
#enter pasword
pass_field=driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys('Farhan@!234')

time.sleep(2)

#login button
login_btn=driver.find_element(By.CLASS_NAME,'submit-btn').click()

time.sleep(15)

#verification code
verification_code=driver.find_element(By.NAME,'name').send_keys('')

time.sleep(5)

#click on next button
next_btn=driver.find_element(By.CLASS_NAME,'submit-btn').click()

time.sleep(5)


#click on view button on project
view_btn=driver.find_elements(By.CLASS_NAME, 'm-auto')
view_btn[0].click()

time.sleep(5)

#click on the files button inside project
files_btn= driver.find_elements(By.CLASS_NAME, 'm-auto')
files_btn[0].click()

time.sleep(5)

#click on sign button
sign_btn= driver.find_elements(By.XPATH,"//button[contains(text(),'Sign')]")
sign_btn[1].click()

time.sleep(5)

#enter the sign
signature=driver.find_element(By.XPATH, "//input[@placeholder='Sign here']").send_keys('Farhan')

time.sleep(5)

#approve the file
#approve_btn=driver.find_element(By.XPATH,"//button[contains(text(),'Approve')]").click()

#reject the file
reject_btn=driver.find_element(By.XPATH,"//button[contains(text(),'Reject')]").click()

time.sleep(10)

#adding a comment
comment=driver.find_element(By.XPATH, "//body/ngb-modal-window[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/textarea[1]").send_keys("I am rejecting the file")

time.sleep(5)

#click on send and reject button
send_reject_btn=driver.find_element(By.XPATH,"//button[contains(text(),'Send and reject')]").click()

time.sleep(10)

driver.close()




















