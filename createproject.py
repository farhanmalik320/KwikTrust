import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)

def setURL():
  #open the url in the browser
  stagingurl= "https://develop-v2.d2ld8gf66npudc.amplifyapp.com/#/auth/login"
  produrl="https://www.app.v2.kwiktrust.com/#/auth/login"

  current_url = driver.get(stagingurl)
  driver.maximize_window()
  time.sleep(2)
  Email= 'Farhan.sharif@ideofuzion.com'
  Password= 'Farhan@1234'
  Verification_code= '123456'

  #enter email
  email_field=driver.find_element(By.XPATH,"//input[@placeholder='Your E-mail']").send_keys(Email)

  time.sleep(2)

  #enter pasword
  pass_field=driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(Password)

  time.sleep(2)

  #login button

  login_btn=driver.find_element(By.CLASS_NAME,'submit-btn').click()

  time.sleep(5)

  #verification code

  verification_code=driver.find_element(By.NAME,'name').send_keys(Verification_code)

  time.sleep(2)

  #click on next button

  next_btn=driver.find_element(By.CLASS_NAME,'submit-btn').click()

  time.sleep(10)

def createproject():

  i = 0
  j = 0
  k = 19
  l = 1
  length= 1

  while i < length:
    projectname = ["Farhan's Project " + str(k)]
    projectlogo = ["F://NFT_s//JNER8//" + str(l) + ".png"]

    # click on create project
    create_project = driver.find_element(By.CLASS_NAME, 'heading').click()

    time.sleep(2)

    #add the project logo
    driver.find_element(By.ID, 'file-input').send_keys(projectlogo)

    time.sleep(2)

    #enter name in project field
    project_field= driver.find_element(By.XPATH, "//input[@placeholder='Project Name']").send_keys(projectname)

    time.sleep(2)

    #click on create button
    create_btn=driver.find_element(By.CLASS_NAME,'create-btn').click()

    time.sleep(5)

    #done button on the popup
    done_btn=driver.find_element(By.CLASS_NAME,'alert-success-class').click()

    time.sleep(2)
    i+=1
    j+=1
    k+=1
    l+=1

setURL()
createproject()
driver.close()




















