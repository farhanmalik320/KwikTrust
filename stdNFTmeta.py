import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options= ChromeOptions()
chrome_options.add_extension("meta.crx")

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s, options=chrome_options)

chrome_options= ChromeOptions()
chrome_options.add_extension("meta.crx")

def MetaMaskSetup():
    driver.switch_to.window(driver.window_handles[0])

    # clicking on get started button
    get_started_button = driver.find_element(By.CLASS_NAME, "first-time-flow__button")
    get_started_button.click()

    # clicking on i agree button
    i_agree = driver.find_element(By.CLASS_NAME, "page-container__footer-button")
    i_agree.click()

    # clicking on import wallet button
    import_wallet = driver.find_element(By.CLASS_NAME, "first-time-flow__button")
    import_wallet.click()

    # Seedphrasefirstword
    driver.find_element(By.ID, "import-srp__srp-word-0").send_keys("refuse")

    # Seedphrasesecondword
    driver.find_element(By.ID, "import-srp__srp-word-1").send_keys("alcohol")

    # Seedphrasethirdword
    driver.find_element(By.ID, "import-srp__srp-word-2").send_keys("anger")

    # Seedphrasefourthword
    driver.find_element(By.ID, "import-srp__srp-word-3").send_keys("same")

    # Seedphrasefifthword
    driver.find_element(By.ID, "import-srp__srp-word-4").send_keys("crumble")

    # Seedphrasesixthword
    driver.find_element(By.ID, "import-srp__srp-word-5").send_keys("amused")

    # Seedphraseseventhword
    driver.find_element(By.ID, "import-srp__srp-word-6").send_keys("space")

    # Seedphraseeighword
    driver.find_element(By.ID, "import-srp__srp-word-7").send_keys("find")

    # Seedphrasenineword
    driver.find_element(By.ID, "import-srp__srp-word-8").send_keys("pigeon")

    # Seedphrasetenword
    driver.find_element(By.ID, "import-srp__srp-word-9").send_keys("razor")

    # Seedphraseelevenword
    driver.find_element(By.ID, "import-srp__srp-word-10").send_keys("fossil")

    # Seedphrasetwleveword
    driver.find_element(By.ID, "import-srp__srp-word-11").send_keys("crime")

    # passwordfield
    driver.find_element(By.ID, "password").send_keys("Farhan@1234")

    # confirmpassword
    driver.find_element(By.ID, "confirm-password").send_keys("Farhan@1234")

    # clickoncheckbox
    driver.find_element(By.ID, "create-new-vault__terms-checkbox").click()

    # importbutton
    driver.find_element(By.CLASS_NAME, "create-new-vault__submit-button").click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "first-time-flow__button")))

    # alldonebutton
    get_started_button = driver.find_element(By.CLASS_NAME, "first-time-flow__button")
    get_started_button.click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "chip__left-icon")))

    # network dropdown
    click_network = driver.find_element(By.CLASS_NAME, 'chip__left-icon').click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "network__add-network-button")))

    # click on addnetwork
    add_network = driver.find_element(By.CLASS_NAME, 'network__add-network-button').click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "form-field__input")))
    # add the text on all the required fields on add network page

    network_name = driver.find_elements(By.CLASS_NAME, 'form-field__input')
    network_name[0].send_keys('Mumbai Testnet')
    network_name[1].send_keys('https://rpc-mumbai.maticvigil.com/')
    network_name[2].send_keys('80001')
    network_name[3].send_keys('MATIC')
    network_name[4].send_keys('https://polygonscan.com/')

    save_btn = driver.find_element(By.CSS_SELECTOR, '.btn--rounded.btn-primary').click()

    time.sleep(5)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)

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

 time.sleep(5)

 #click on view button on project
 view_btn=driver.find_elements(By.CLASS_NAME, 'm-auto')
 view_btn[0].click()

 time.sleep(2)

 #click on the files button inside project
 files_btn= driver.find_elements(By.CLASS_NAME, 'm-auto')
 files_btn[0].click()

 time.sleep(5)

def connectwallet():

    #click on the start button
    start_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Start')]").click()

    time.sleep(5)

    #click on the connect wallet button
    connect_wallet_btn= driver.find_element(By.XPATH,"//button[contains(text(),'Connect')]").click()

    time.sleep(5)

    # sets the metamask extension ID
    EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'

    # switch to Metamask extension
    driver.switch_to.window(driver.window_handles[0])

    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html'.format(EXTENSION_ID))

    time.sleep(5)
    # click on the next button in MetaMask
    next_btn = driver.find_element(By.CSS_SELECTOR, '.btn--rounded.btn-primary').click()

    time.sleep(5)

    connect_btn = driver.find_element(By.CSS_SELECTOR, '.btn--rounded.btn-primary').click()

    time.sleep(5)

    # switch to kwiktrust extension
    driver.switch_to.window(driver.window_handles[1])

    time.sleep(5)

    standard_nft_btn= driver.find_elements(By.CLASS_NAME,'m-auto')
    standard_nft_btn[0].click()

    time.sleep(5)

def uploadfiles():
    i = 0
    length = 1
    fileno = 7
    filename = 1

    while i < length:
        j = 0
        k = 0
        foldername = "F://NFT_s//TestFolder//"
        nftfilepatharray = [foldername + str(fileno) + ".png"]
        nftfilename = ["Standard NFT" + str(filename)]
        nftfiledescription = ["Standard NFT" + str(filename) + "Description"]

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '+ Upload file')]")))

        time.sleep(1)

        upload_files_btn = driver.find_element(By.XPATH, "//button[contains(text(), '+ Upload file')]").click()

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "undefined")))

        upload_file = driver.find_element(By.ID, 'undefined').send_keys(nftfilepatharray)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Name of file']")))

        file_name = driver.find_element(By.XPATH, "//input[@placeholder='Name of file']").send_keys(nftfilename)

        file_description = driver.find_element(By.XPATH, "//input[@placeholder='Description of file']").send_keys(
            nftfiledescription)

        # select file type

        file_type = driver.find_elements(By.CLASS_NAME, 'documentType')

        file_type[4].click()

        next_btn = driver.find_element(By.CLASS_NAME, 'width100-pre').click()

        i += 1
        j += 1
        k += 1
        fileno += 1
        filename += 1
        time.sleep(5)


def mintNFT():

    #click on an image
    image = driver.find_elements(By.CLASS_NAME, 'image-section')
    nftlength=len(image)
    print(nftlength)

    i=0
    while i < nftlength:
        image = driver.find_elements(By.CLASS_NAME, 'image-section')
        image[i].click()
        i += 1

    time.sleep(5)

    #click on Mint button
    mint_btn= driver.find_element(By.CLASS_NAME, 'color-white').click()

    time.sleep(5)

    #click on firsy radio
    radio_btn=driver.find_elements(By.NAME,'copyright')
    radio_btn[0].click()

    time.sleep(2)

    #click on next button
    next_btnn= driver.find_element(By.XPATH,"//button[contains(text(), 'Next')]").click()

    time.sleep(5)

    #click on currency drop down
    select_dropdown=driver.find_element(By.XPATH,"//span[contains(text(),'Select')]").click()

    time.sleep(2)

    #select KTX
    select_KTX= driver.find_element(By.XPATH, "//div[contains(text(),'KTX')]").click()

    time.sleep(5)

    #click on pay buttpn
    pay_btn=driver.find_element(By.XPATH,"//button[contains(text(),'PAY')]").click()

    time.sleep(5)

    #click on Next button
    next_btn_mint= driver.find_element(By.XPATH,"//button[contains(text(),'Next')]").click()

    time.sleep(10)

    EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'

    # switch to Metamask extension
    driver.switch_to.window(driver.window_handles[0])

    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html'.format(EXTENSION_ID))

    time.sleep(15)
    # click on the next button in MetaMask
    next_btn = driver.find_element(By.CSS_SELECTOR, '.btn--rounded.btn-primary').click()

    time.sleep(15)

    #driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html'.format(EXTENSION_ID))

    #time.sleep(15)
    # click on the next button in MetaMask
    #next_btn = driver.find_element(By.CSS_SELECTOR, '.btn--rounded.btn-primary').click()


    #time.sleep(15)

    driver.switch_to.window(driver.window_handles[1])

    time.sleep(60)

    next_btn_mint = driver.find_element(By.XPATH, "//button[@id='okButton']").click()

    print("NFT Minted by MetaMask successfully")


setURL()
MetaMaskSetup()
login()
connectwallet()
uploadfiles()
mintNFT()




























