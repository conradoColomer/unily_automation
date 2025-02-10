from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EcommerceAutomation:
    def __init__(self, driver):
        self.driver = driver
        self.CONTINUE_SHOPPING_BUTTON = (By.CLASS_NAME, 'continue-shopping')  # Ajusta el selector si es necesario

    # Método para esperar el elemento y hacer clic en el botón "Continue Shopping"
    def click_continue_shopping_button(self):
        button = self.wait_for_element(self.CONTINUE_SHOPPING_BUTTON)
        # Espera a que el botón sea clickeable y hace clic en él
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button))
        button.click()

    # Método para esperar un elemento (se puede personalizar para otros casos)
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    # Método para interactuar con los primeros 'n' productos
    def interactuar_con_productos(self, cantidad_productos):
        productos = self.driver.find_elements(By.CLASS_NAME, "single-products")

        # Asegurarse de no exceder el número de productos disponibles
        for i in range(min(cantidad_productos, len(productos))):
            # Encuentra el botón "Add to cart" dentro del producto
            boton_agregar_carrito = productos[i].find_element(By.XPATH, ".//a[@class='btn btn-default add-to-cart']")
            boton_agregar_carrito.click()  # Hace clic en "Add to cart"

            # Ejecuta el método para continuar comprando
            self.click_continue_shopping_button()

            # Opcionalmente puedes agregar algún tipo de espera entre clics para simular un comportamiento más real
            WebDriverWait(self.driver, 2)  # Espera de 2 segundos entre clics (ajusta si es necesario)


# Inicializa el driver y la clase
driver = webdriver.Chrome()
driver.get("https://automationexercise.com")

# Crea una instancia de la clase y pasa la cantidad de productos con los que deseas interactuar
ecommerce_automation = EcommerceAutomation(driver)
ecommerce_automation.interactuar_con_productos(2)  # Cambia el número según lo necesites

# Cierra el navegador al final
driver.quit()