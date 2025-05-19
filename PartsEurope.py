from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def run(driver, product_code, username, password):
    wait = WebDriverWait(driver, 10)

    def try_click(by, selector, timeout=5):
        try:
            elem = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, selector))
            )
            elem.click()
            return True
        except TimeoutException:
            return False

    try:
        driver.get("https://partseurope.eu/en/")

        print("Пытаемся кликнуть на кнопку куки...")
        try_click(By.CSS_SELECTOR, "button.yes-to-all.btn.btn-primary.btn-md.save-information")

        print("Пытаемся кликнуть на кнопку подтверждения страны...")
        try_click(By.CSS_SELECTOR, "button.btn.btn-primary.btn-md.save-information")

        print("Кликаем на кнопку 'Log in'...")
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']")))
        login_button.click()

        print("Вводим email...")
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "_email")))
        email_input.clear()
        email_input.send_keys(username)

        print("Вводим пароль...")
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "_password")))
        password_input.clear()
        password_input.send_keys(password)

        print("Кликаем кнопку 'Login'...")
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary.btn-lg.btn-icon")))
        submit_button.click()
        time.sleep(7)

        print("Ожидаем поле поиска...")
        search_input = wait.until(EC.presence_of_element_located((By.ID, "s")))

        print(f"Вводим код товара: {product_code}")
        search_input.clear()
        search_input.send_keys(product_code)

        print("Нажимаем кнопку поиска...")
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        search_button.click()

        print("Ожидаем результаты...")

    finally:
        print("Закончили с PartsEurope")
        return driver
