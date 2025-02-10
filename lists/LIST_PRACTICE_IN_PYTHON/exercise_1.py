# EJERCICIO 1: Obtener y contar una lista de elementos en Selenium
# Objetivo: Extraer todos los elementos de una lista y contar cuántos hay.

# 1. Abre un navegador con Selenium y carga una página web de prueba.
# 2. Encuentra todos los elementos de una lista de productos usando find_elements().
# 3. Imprime la cantidad total de elementos encontrados.
# 4. Cierra el navegador.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa el driver y la clase
driver = webdriver.Chrome()
driver.get("https://automationexercise.com")

LIST_XPATH = (By.XPATH, "//div[contains(@class, 'productinfo text-center')]//p")

productos =  WebDriverWait(driver,10).until(EC.presence_of_all_elements_located(LIST_XPATH))

print(f"La cantidad de elementos ubicados es de: {len(productos)}")
# Cierra el navegador al final
driver.quit()