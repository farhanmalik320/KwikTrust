import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)

def setURL():
    # open the url in the browser
    stagingurl = "https://develop-v2.d2ld8gf66npudc.amplifyapp.com/#/auth/login"
    produrl = "https://www.app.v2.kwiktrust.com/#/auth/login"
    localhost= "http://192.168.101.130:4300/#/auth/login"
    current_url = driver.get(stagingurl)
    driver.maximize_window()

def login():

 #login details
 Email= 'farhan.sharif@ideofuzion.com'
 Password='Farhan@1234'
 verificationcode='123456'

 #enter email
 email_field=driver.find_element(By.XPATH, "//input[@placeholder='Your E-mail']").send_keys(Email)

 #enter pasword

 pass_field=driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(Password)

 #login button
 login_btn=driver.find_element(By.CLASS_NAME,'submit-btn').click()

 WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'name')))

 #verification code
 verification_code=driver.find_element(By.NAME,'name').send_keys(verificationcode)

 time.sleep(1)

 #click on next button
 next_btn=driver.find_element(By.CLASS_NAME,'submit-btn').click()

 time.sleep(1)

 WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'm-auto')))
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".reply-button”))

 #click on view button on project
 view_btn=driver.find_elements(By.CLASS_NAME, 'm-auto')
 view_btn[0].click()

 time.sleep(2)

 WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'm-auto')))

 #click on the files button inside project
 files_btn= driver.find_elements(By.CLASS_NAME, 'm-auto')
 files_btn[4].click()

 time.sleep(3)

def createfolder():

    i=0
    j=1
    length=1
    while i<length:

      wait = WebDriverWait(driver, 10)
      element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn')))
      #click on the add folder button
      add_folder_btn= driver.find_elements(By.CLASS_NAME, 'btn')
      add_folder_btn[1].click()

      time.sleep(5)

      #create a folder
      Foldername = ["Folder no " + str(j)]

      folder_input= driver.find_element(By.XPATH,"//input[@placeholder='Folder Name']").send_keys(Foldername)

      time.sleep(5)

      create_btn= driver.find_element(By.CLASS_NAME,'create-btn').click()

      time.sleep(5)

      i+=1
      j+=1

def uploadfiles():

    time.sleep(5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'm-auto')))
    #click on the view button on folder
    view_btn = driver.find_elements(By.CLASS_NAME, 'm-auto')
    view_btn[1].click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,'custom-success-btn')))

    #click on the add file button
    add_file_btn= driver.find_element(By.CLASS_NAME,'custom-success-btn').click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "undefined")))

    upload_file=driver.find_element(By.ID,'undefined').send_keys("F://NFT_s//lifejoke//12.png")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Name of file']")))

    FileName= 'My Test File for 50 Signatories'
    FileDescription= 'My Test Description'

    file_name= driver.find_element(By.XPATH, "//input[@placeholder='Name of file']").send_keys(FileName)

    time.sleep(1)

    file_description = driver.find_element(By.XPATH, "//input[@placeholder='Description of file']").send_keys(FileDescription)

    time.sleep(1)

    #select file type
    file_type= driver.find_elements(By.CLASS_NAME,'documentType')
    file_type[4].click()

    time.sleep(1)

    next_btn=driver.find_element(By.CLASS_NAME,'width100-pre').click()

    time.sleep(2)

    length = 25
    emailid = 0
    i = 0
    j = 0
    k = 0
    while i < length:
        signatorieslist = ["sohail" + str(emailid) + "@yopmail.com"]
        signatoriesfirstname = ["sohail" + str(emailid)]
        signatoriessurname = ["sohail" + str(emailid)]

        #click on add signatory icon

        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "//body/app-root[1]/app-full-layout[1]/div[1]/main[1]/app-add-signatory[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/div[1]/img[1]")))

        plus_icon=driver.find_element(By.XPATH,'//body/app-root[1]/app-full-layout[1]/div[1]/main[1]/app-add-signatory[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/div[1]/img[1]').click()

        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Name']")))

        signatory_name = driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys(signatoriesfirstname)

        signatory_surname=driver.find_element(By.XPATH, "//input[@placeholder='Surname']").send_keys(signatoriessurname)

        signatory_email= driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(signatorieslist)

        #select priority

        must_sign=driver.find_elements(By.NAME,'priority')

        must_sign[0].click()

        #required KYC

        required_kyc = driver.find_elements(By.NAME, 'required_identity')

        required_kyc[1].click()

        add_btn= driver.find_element(By.XPATH,"//button[contains(text(),'ADD')]").click()

        i += 1
        k += 1
        j += 1
        emailid += 1

    #add message
    add_message=driver.find_element(By.XPATH,"//input[@placeholder='Write a Message for signatories']").send_keys("Please verify my file")

    time.sleep(2)

    #click on send button
    send_btn= driver.find_element(By.XPATH," //button[contains(text(), 'Send')]").click()

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Homepage')]")))

    #click on homepage button
    homepage_btn= driver.find_element(By.XPATH,"//button[contains(text(), 'Homepage')]").click()

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
driver.close()




























