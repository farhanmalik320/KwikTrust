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
 time.sleep(2)

 #enter pasword

 pass_field=driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(Password)
 time.sleep(2)

 #login button
 login_btn=driver.find_element(By.CLASS_NAME,'submit-btn').click()

 time.sleep(5)

 #verification code
 verification_code=driver.find_element(By.NAME,'name').send_keys(verificationcode)

 time.sleep(5)

 #click on next button
 next_btn=driver.find_element(By.CLASS_NAME,'submit-btn').click()

 time.sleep(10)

 #click on view button on project
 view_btn=driver.find_elements(By.CLASS_NAME, 'm-auto')
 view_btn[0].click()

 time.sleep(5)

 #click on the files button inside project
 files_btn= driver.find_elements(By.CLASS_NAME, 'm-auto')
 files_btn[4].click()

 time.sleep(5)

def uploadfiles():
    #click on the view button on folder
    view_btn = driver.find_elements(By.CLASS_NAME, 'm-auto')
    view_btn[1].click()

    time.sleep(5)

    #click on the add file button
    add_file_btn= driver.find_element(By.CLASS_NAME,'custom-success-btn').click()

    time.sleep(5)

    filepath = ["F://NFT_s//azuka//1.png"]

    upload_file=driver.find_element(By.ID,'undefined').send_keys(filepath)

    time.sleep(5)

    FileName= 'My Test File 2'

    FileDescription= 'My Test Description'

    file_name= driver.find_element(By.XPATH, "//input[@placeholder='Name of file']").send_keys(FileName)

    time.sleep(2)

    file_description = driver.find_element(By.XPATH, "//input[@placeholder='Description of file']").send_keys(FileDescription)

    time.sleep(2)

    #select file type
    file_type= driver.find_elements(By.CLASS_NAME,'documentType')
    file_type[4].click()

    time.sleep(2)
    next_btn=driver.find_element(By.CLASS_NAME,'width100-pre').click()

    time.sleep(2)

    signatorieslist = ["testautomationsignatory@yopmail.com"]
    signatoriesfirstname = ["farhan"]
    signatoriessurname = ["farhansurname"]


    length = len(signatorieslist)

    i = 0
    j = 0
    k = 0
    while i < length:

      #click on add signatory icon

      time.sleep(5)

      plus_icon=driver.find_element(By.XPATH,'//body/app-root[1]/app-full-layout[1]/div[1]/main[1]/app-add-signatory[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/div[1]/img[1]').click()

      time.sleep(5)

      signatory_name = driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys(signatoriesfirstname[j])

      time.sleep(2)

      signatory_surname=driver.find_element(By.XPATH, "//input[@placeholder='Surname']").send_keys(signatoriessurname[k])

      time.sleep(2)

      signatory_email= driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(signatorieslist[i])

      time.sleep(2)

      #select priority

      must_sign=driver.find_elements(By.NAME,'priority')

      must_sign[0].click()

      time.sleep(2)

      #required KYC

      required_kyc = driver.find_elements(By.NAME, 'required_identity')

      required_kyc[1].click()

      time.sleep(5)

      add_btn= driver.find_element(By.XPATH,"//button[contains(text(),'ADD')]").click()

      i += 1
      k += 1
      j += 1
      time.sleep(2)

    #add message
    add_message=driver.find_element(By.XPATH,"//input[@placeholder='Write a Message for signatories']").send_keys("Please verify my file")

    time.sleep(2)

    #click on send button
    send_btn= driver.find_element(By.XPATH," //button[contains(text(), 'Send')]").click()

    time.sleep(15)

    #click on homepage button
    homepage_btn= driver.find_element(By.XPATH," //button[contains(text(), 'Homepage')]").click()

    time.sleep(5)

    # file
    file_btn=driver.find_element(By.XPATH, "//a[contains(text(),'View')]").click()

    time.sleep(5)

    #close the file popup
    close_btn=driver.find_element(By.CLASS_NAME,'close').click()

    time.sleep(5)

    #click on the view file button
    view_file_btn=driver.find_element(By.XPATH,"//button[contains(text(),'View file')]").click()


setURL()
login()
#createfolder()
uploadfiles()





























