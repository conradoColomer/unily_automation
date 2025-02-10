from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializa el navegador
driver = webdriver.Chrome()

# Abre la página web
driver.get("https://automationexercise.com")

# Encuentra todos los <div> con la clase 'single-products'
productos = driver.find_elements(By.CLASS_NAME, "single-products")

# Acceder a los productos por índice
for i, producto in enumerate(productos):
    print(f"Accediendo al producto {i + 1}")  # Opcional, para ver el número de producto
    # Aquí puedes realizar alguna acción, por ejemplo, hacer clic en el botón "Add to cart"
    boton = producto.find_element(By.CLASS_NAME, "add-to-cart")
    boton.click()  # Hace clic en el botón "Add to cart"

# Cierra el navegador
driver.quit()