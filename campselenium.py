from selenium import webdriver #selenium; manuel işlemlerin otomotize edilmesi
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome() #(ChromeDriverManager().install())
#selenium'un çalışması için 'driver' adında değişken tanımlandı.Kullanılacak tarayıcı seçilmelidir.
driver.maximize_window()
driver.get("https://www.google.com/")
sleep(5)
input = driver.find_element(By.NAME,"q")
input.send_keys("kodlamaio")
searchButton = driver.find_element(By.NAME, "btnK") #+Keys.ENTER
sleep(2)
searchButton.click()
sleep(2)
firstResult = driver.find_element(By.PARTIAL_LINK_TEXT, "Kodlama.io")
firstResult.click()
sleep(2)
listOfCourse = driver.find_elements(By.CLASS_NAME, "course-listing-title")
print(f"Kodlama sitesinde şu anda {len(listOfCourse)} adet kurs var.") #listelerin uzunluğu len fonksiyonuyla alınıyor.


#FULL XPATH
#/html/body/div[1]/div[3]/div/div/div[1]/div/div/div/div/ol/li[1]/div/div[1]/h3/a
#XPATH
#//*[@id="web"]/ol/li[1]/div/div[1]/h3/a
# örnek xpath bulma: //textarea[@class='gLFyf']
while True:  
    continue   #sonsuz döngü.


#HMTL LOCATORS; hmtl'deki elementlerin konumunu öğrenmek.