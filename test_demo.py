
#prefix -> ön ek test_, test gibi davranıp ona göre davranıyor.
#postfix -> 
#test ön ekiyle çalışması önemlidir.

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions #as ec de olur #bekleme işlemini hangi şarta bağlı olarak yükleneceğini belirtir.
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class Test_DemoClass:
    def setup_method(self): #her testten önce çağrılır.
        self.driver = webdriver.Chrome()
        self.driver.maximize_window
        self.driver.get("https://www.saucedemo.com/")
    
    
    def teardown_method(self): #her testten sonra çağrılır.
        self.driver.quit()
    
    
    def test_demoFunc(self):
        #3A Arrange Assert
        text = "Hello"
        assert text == "Hello" #assert; ilgili testin bağlı olduğu condition'ı belirtmek demektir. Testin sonuçlanmasıdır.
        #testRseult yerine ASSERT
    def test_demo2(self):
        assert True

    #@pytest.mark.skip(); bu fonksiyonu atla demektir.
    @pytest.mark.parametrize("username,password", [("1","1") , ("kullaniciadim", "sifrem")])
    def test_invalid_login(self, username, password):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
        # en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys(username)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys(password)
        login = self.driver.find_element(By.ID, "login-button")
        login.click()
        errorMessage = self.driver.find_element(By.XPATH, "//div[@class='error-message-container error']")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"


