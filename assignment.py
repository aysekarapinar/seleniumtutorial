from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class work():

    def incorrectConditions(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        sleep(5)
        username=self.driver.find_element(By.ID,"user-name")
        username.send_keys("")
        password=self.driver.find_element(By.XPATH,"//input[@name='password']")
        password.send_keys("")
        logginButton=self.driver.find_element(By.NAME,"login-button")
        logginButton.click()
        sleep(2)
        errorMassage=self.driver.find_element(By.XPATH,"//div[@class='error-message-container error']")
        testResult=errorMassage.text=="Epic sadface: Username is required"
        print(f"test result:{testResult}")
    
    def passwordEmpty(self):
        username=self.driver.find_element(By.ID,"user-name")
        username.send_keys("pair4")
        sleep(2)
        password=self.driver.find_element(By.XPATH,"//input[@name='password']")
        password.send_keys("")
        logginButton=self.driver.find_element(By.NAME,"login-button")
        logginButton.click()
        sleep(3)
        errorMassage=self.driver.find_element(By.XPATH,"//div[@class='error-message-container error']")
        testResult=errorMassage.text=="Epic sadface: Password is required"
        print(f"testResult:{testResult}")
        if testResult==True:
            username.clear()
        sleep(2)
    
    def incorrectUsername(self):
         username=self.driver.find_element(By.ID,"user-name")
         username.send_keys("locked_out_user")
         sleep(2)
         password=self.driver.find_element(By.XPATH,"//input[@name='password']")
         password.send_keys("secret_sauce")
         logginButton=self.driver.find_element(By.NAME,"login-button")
         logginButton.click()
         sleep(3)
         errorMassage=self.driver.find_element(By.XPATH,"//div[@class='error-message-container error']")
         testResult=errorMassage.text=="Epic sadface: Sorry, this user has been locked out."
         print(f"testResult:{testResult}")
         if testResult==True:
             username.clear()
    sleep(10)
             
    

    def login(self):
        username=self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        sleep(2)
        password=self.driver.find_element(By.XPATH,"//input[@name='password']")
        password.send_keys("")
        sleep(3)
        logginButton=self.driver.find_element(By.NAME,"login-button")
        logginButton.click()
        sleep(3)
        baslik=self.driver.find_element(By.XPATH,"//div[@class='app_logo']")
        testResult=baslik.text=="Swag Labs"

        if testResult==True:

         print("ANASAYFAYA GİRİŞ YAPTINIZ.")

    def addtocart(self):
        light=self.driver.find_element(By.XPATH,"//a[@data-test='item-0-title-link']")
        light.click()
        sleep(3)
        button=self.driver.find_element(By.ID,"add-to-cart")
        button.click()
        sleep(3)

         
        
       
test=work()
test.incorrectConditions()
test.passwordEmpty()
test.incorrectUsername()
test.login()
test.addtocart()



