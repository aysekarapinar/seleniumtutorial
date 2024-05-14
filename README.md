PyTest decoratorler nedir? 
parametre olarak fonksiyon alan, geriye fonksiyon döndüren fonksiyonlardır. Decoratorler fonksiyonun önüne @ işareti konularak oluşturulur. Buna 'pie syntax' denir.
Python'da test yazma ve çalıştırma sürecini kolaylaştırır.
Birkaç decorator örneği;

@pytest.fixture, test fonksiyonlarının gerekli kaynakları (veritabanı bağlantıları, dosya işlemleri, ağ bağlantıları vb.) ayarlamak için kullanılır.
@pytest.mark, test fonksiyonlarına özel etiketler eklemek için kullanılır. Bu, belirli koşullarda testlerin çalıştırılmasını veya belirli gruplara dahil edilmesini sağlar.

import pytest

@pytest.fixture
def setup():
    # Test ortamını hazırla
    ...

@pytest.mark.smoke
def test_login():
    # Giriş testini yap
    ...

@pytest.mark.regression
def test_checkout():
    # Satın alma işlemi testini yap
    ...
