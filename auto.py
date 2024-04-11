from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome()
driver.get("https://void.co.mz/")


#teste de formulário
try:
    field_nome = driver.find_element(By.ID, 'form-field-name')
    field_nome.send_keys("Germano")

    field_email = driver.find_element(By.ID, 'form-field-email')
    field_email.send_keys("Germano.kazembe@gmail.com")

    field_mensagem = driver.find_element(By.ID, 'form-field-message')
    field_mensagem.send_keys("Teste de submissão automática de dados 1")

    submit_button = driver.find_element(By.XPATH, '//*[@id="get-in-touch"]/div/div[2]/div/div/div/form/div/div[5]/button/span')
    submit_button.click()

    time.sleep(5)

except Exception as e:
    print("Erro ao extrair:", e)

finally:
    pass


#Teste de responsividade
driver.set_window_size(height=930,width=200)

#clicka no menu blog
blog = driver.find_element(By.XPATH,'//*[@id="menu-item-55"]/a/span[1]/span')
blog.click()
time.sleep(1)

#clicka no menu jobar
jobar = driver.find_element(By.XPATH,'//*[@id="menu-item-56"]/a/span[1]/span')
jobar.click()
time.sleep(1)

#clicka no menu oi
oi = driver.find_element(By.XPATH,'//*[@id="menu-item-57"]/a/span[1]/span')
oi.click()
time.sleep(1)

#clicka no menu home
home = driver.find_element(By.XPATH,'//*[@id="menu-item-58"]/a/span[1]/span')
home.click()

time.sleep(10)

driver.set_window_size(height=930,width=700)

driver.quit()


