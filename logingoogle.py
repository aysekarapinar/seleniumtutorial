from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #anahtarları içe aktarıyor.
from selenium.webdriver.support.ui import WebDriverWait #bir elementin var olmasını beklemek istiyorsak.
from selenium.webdriver.support import expected_conditions as EC #ilerlemeden önce bir elementin varlığını tekrar beklememize izin verecek.


driver = webdriver.Chrome() #tarayıcının hangi browser olduğunu belirtiyorum.
driver.maximize_window()
driver.get("https://google.com") # 'get' ile hangi siteye gideceğimi belirtiyorum.
input_element = driver.find_element(By.CLASS_NAME,"gLFyf") #sayfaki öğeyi bulup onunla iletişim kurmak.
input_element.clear() #temizleme yöntemi.
input_element.send_keys("selenium" +Keys.ENTER) #anahtar kelimeler göndermek ve üzerine tıklayabilmek. Bir şeyler yazmamızı sağlıyor.

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium") #linklerin içindeki metini eşleştirmek için kullanılır.
link.click()

sleep(10) #sitenin kaç saniye açık duracağını belirtiyorum.
driver.quit() #sürücüden çıkabiliyoruz.