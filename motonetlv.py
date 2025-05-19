from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
        driver.get("https://motonetlv.lv/")

        if try_click(By.CSS_SELECTOR, "span.arrowTransform.glyphicon.glyphicon-menu-down"):
            print("Раскрыли форму входа")
        else:
            print("Кнопка раскрытия формы входа не найдена или не требуется")

        login_input = wait.until(EC.element_to_be_clickable((By.ID, "login")))
        login_input.clear()
        login_input.send_keys(username)
        print("Логин введен")

        password_input = wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_input.clear()
        password_input.send_keys(password)
        print("Пароль введен")

        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.mButton[value='Ienākt']")))
        login_button.click()
        print("Нажата кнопка входа")

        time.sleep(1)

        search_input = wait.until(EC.element_to_be_clickable((By.ID, "fulltextsearch")))
        search_input.click()
        print("Поле поиска готово")

        search_input.clear()
        search_input.send_keys(product_code)
        search_input.send_keys(Keys.ENTER)
        print(f"Выполнен поиск по коду товара: {product_code}")

    finally:
        print("Закончили с MotonetLV")
        return driver
