import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions


s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)

def setURL():
  #open the url in the browser
  current_url = driver.get("https://develop-v2.d2ld8gf66npudc.amplifyapp.com/#/auth/login")
  driver.maximize_window()
  time.sleep(2)

def login():

 #login details
 Email= 'farhan.sharif@ideofuzion.com'
 Password='Farhan@1234'
 verificationcode='123456'

 #enter email
 email_field=driver.find_element(By.XPATH, "//input[@placeholder='Your E-mail']").send_keys(Email)
 time.sleep(1)

 #enter pasword

 pass_field=driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(Password)
 time.sleep(1)

 #login button
 login_btn=driver.find_element(By.CLASS_NAME,'submit-btn').click()

 time.sleep(5)

 #verification code
 verification_code=driver.find_element(By.NAME,'name').send_keys(verificationcode)

 time.sleep(2)

 #click on next button
 next_btn=driver.find_element(By.CLASS_NAME,'submit-btn').click()

 time.sleep(5)

 #click on view button on project
 view_btn=driver.find_elements(By.CLASS_NAME, 'm-auto')
 view_btn[0].click()

 time.sleep(2)

 #click on the super NFT button inside project
 files_btn= driver.find_elements(By.CLASS_NAME, 'm-auto')
 files_btn[0].click()

 time.sleep(5)

def transferNFT():
    #click on the view button
    view_btn = driver.find_elements(By.CLASS_NAME, "w-100")
    print(len(view_btn))
    view_btn[2].click()
    time.sleep(5)

    #click on transfer button
    transfer_btn= driver.find_element(By.XPATH,"//button[contains(text(),'Transfer')]").click()

    time.sleep(5)

    #input wallet address
    wallet_address= '0bef2dc17a6f42f985c802d9a4e500c6cf30209c789e790d832d620976caf484'
    receiver_wallet= driver.find_element(By.XPATH, "//input[@placeholder='Wallet address']").send_keys(wallet_address)

    time.sleep(5)

    #click on send button
    send_btn= driver.find_element(By.XPATH, "//button[contains(text(),'Send')]").click()

    time.sleep(10)

    # verification code
    verification_code = driver.find_element(By.NAME, 'name').send_keys('')

    time.sleep(5)

    # click on next button
    next_btn = driver.find_element(By.CLASS_NAME, 'submit-btn').click()

    time.sleep(5)

    # click on currency drop down
    select_dropdown = driver.find_element(By.XPATH, "//span[contains(text(),'Select')]").click()

    time.sleep(2)

    # select USD
    select_KTX = driver.find_element(By.XPATH, "//div[contains(text(),'USD')]").click()

    time.sleep(5)

    # click on pay buttpn
    pay_btn = driver.find_element(By.XPATH, "//button[contains(text(),'PAY')]").click()

    time.sleep(10)

    #  driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))  # First iframe
    iframe_by_title = driver.find_element(By.XPATH, "//iframe[@title='Secure payment input frame']")
    driver.switch_to.frame(iframe_by_title)

    # Enter card number
    cardnumber = "4242424242424242"
    expirydate = "2/23"
    cvc = "1234"

    creditNumber = driver.find_element(By.ID, "Field-numberInput").send_keys("4242 4242 4242 4242")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@placeholder='MM / YY']").send_keys(expirydate)
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@placeholder='CVC']").send_keys(cvc)
    time.sleep(1)

    driver.switch_to.default_content()

    time.sleep(2)

    pay_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Pay')]").click()

    time.sleep(10)
    print("NFT Transfer by card successfully")
    driver.close()


setURL()
login()
transferNFT()




























