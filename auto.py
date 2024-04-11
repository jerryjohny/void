from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

# Para abrir a página
driver.get("https://void.co.mz/")


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
    # Fecha o navegador
    driver.quit()

# nome = field_nome.text.strip()