from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions #as ec de olur #bekleme işlemini hangi şarta bağlı olarak yükleneceğini belirtir.
from selenium.webdriver.common.action_chains import ActionChains
class Test_Sauce:
    def __init__(self):    #driver'ı class'ın içine taşımış oldu.
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    
    def test_invalid_login(self): #kişinin doğru giriş yapmadığı senaryoyu test edecek senaryo.
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
        # en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("1")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys("1")
        login = self.driver.find_element(By.ID, "login-button")
        login.click()
        errorMessage = self.driver.find_element(By.XPATH, "//div[@class='error-message-container error']")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"test result: {testResult}")
    
    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
        passwordInput = self.driver.find_element(By.ID, "password")
        #Action Chains: aksiyonlarımızı zincir misali birbiri ardına bağlanması, bu sırada kullanmasını sağlayan bir yapı.
        actions = ActionChains(self.driver) #aksiyon dizisi. Tek bir element üzerinde birden fazla işlem yapılacağı zaman kullanılır.
        actions.send_keys_to_element(usernameInput, "standard_user")
        actions.send_keys_to_element(passwordInput, "secret_sauce")
        actions.perform()
        #usernameInput.send_keys("standard_user")
        #passwordInput.send_keys("secret_sauce")
        login = self.driver.find_element(By.ID, "login-button")
        login.click()
        self.driver.execute_script("window.scrollTo(0,500)")
        
testClass=Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()

