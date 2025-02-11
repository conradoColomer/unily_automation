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
from selenium.webdriver.chrome.options import Options

# Inicializa el driver y la clase
options = Options()
options.add_argument("--headless")  # Ejecuta el navegador en segundo plano
driver = webdriver.Chrome(options=options)
driver.get("https://automationexercise.com")
wait = WebDriverWait(driver,10)

#Localizadores
PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'productinfo text-center')]//p")
RS_NAME =  (By.XPATH, "//div[contains(@class, 'productinfo text-center')]//h2")

#Extraccion
producto = [elemento.text for elemento in wait.until(EC.presence_of_all_elements_located(PRODUCT_NAME))]
rs_de_productos = [elemento.text for elemento in wait.until(EC.presence_of_all_elements_located(RS_NAME))]

# Cierra el navegador al final
driver.quit()


#Combinando dos listas
lista_de_productos = []
for producto, rs_de_productos in  zip(producto,rs_de_productos):
        lista_de_productos.append({"Producto" : producto, "RS" : rs_de_productos})

#Iteramos la lista para obtener solo los productos con 'Dress'
for item in lista_de_productos:
    if " Dress" in item['Producto']:
        print(f'Producto valido: {item['Producto']}')
    else:
        continue

