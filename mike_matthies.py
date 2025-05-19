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
        driver.get("https://mike.matthies.de/en")

        # 1. Кликаем на куки
        print("Пытаемся принять куки...")
        try_click(By.CSS_SELECTOR, "div#dv-t3-consent-management-button-accept-all.btnAcceptAll")
        time.sleep(1)

        # 2. Вводим логин
        print("Вводим логин...")
        login_input = wait.until(EC.presence_of_element_located((By.NAME, "mcustno")))
        login_input.clear()
        login_input.send_keys(username)

        # 3. Вводим пароль
        print("Вводим пароль...")
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "mpassword")))
        password_input.clear()
        password_input.send_keys(password)

        # 4. Кликаем кнопку логина
        print("Кликаем кнопку 'Login'...")
        login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "smbtn")))
        login_button.click()

        time.sleep(1)  # ждём загрузку после входа

        # 5. Ждём поле поиска
        print("Ожидаем поле поиска...")
        search_input = wait.until(EC.presence_of_element_located((By.ID, "asuche")))

        # 6. Вводим код товара и запускаем поиск через кнопку
        print(f"Вводим код товара: {product_code}")
        search_input.clear()
        search_input.send_keys(product_code)

        print("Нажимаем кнопку поиска...")
        search_button = wait.until(EC.element_to_be_clickable((By.ID, "suche-button")))
        search_button.click()

        print("Ожидаем результаты...")

    finally:
        print("Закончили с Mike Matthies")
        return driver
