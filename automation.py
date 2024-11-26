from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import traceback
import time

# Configurar o driver (exemplo com ChromeDriver)
driver = webdriver.Chrome()

try:
    # Passo 1: Acesse a tela de produtos
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    print("Página carregada com sucesso.")
    
    # Passo 2: Faça login
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(1)
    print("Login realizado com sucesso.")

    # Esperar a página carregar completamente
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inventory_container"]')))
    print("Página de produtos carregada.")
    
    # Passo 3: Adicione um produto ao carrinho
    add_to_cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')))
    add_to_cart_button.click()
    print("Produto adicionado ao carrinho.")
    
    # Passo 4: Verifique o contador
    cart_counter = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), "1"))
    print("Contador atualizado para 1.")
    time.sleep(2)
    cart_counter = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(2)
    # Passo 5: Remover o produto do carrinho
    remove_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')))
    remove_button.click()
    print("Produto removido do carrinho.")
    time.sleep(1)

    # Verifique se o contador foi atualizado para 0
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="shopping_cart_container"]/a'), ""))
    time.sleep(1)
    print("Contador atualizado para 0.")
    print("Teste concluído com sucesso.")

except Exception as e:
    print(f"Erro durante o teste: {e}")

finally:
    driver.quit()   
