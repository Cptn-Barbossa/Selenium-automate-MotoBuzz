from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

from PartsEurope import run as run_parts
from mike_matthies import run as run_mike
from motonetlv import run as run_motonet

from dotenv import load_dotenv
import os

load_dotenv()

parts_username = os.getenv("MOTOBUZZ_PARTS_USERNAME")
parts_password = os.getenv("MOTOBUZZ_PARTS_PASSWORD")

mike_username = os.getenv("MOTOBUZZ_MATTHIES_USERNAME")
mike_password = os.getenv("MOTOBUZZ_MATTHIES_PASSWORD")

motonet_username = os.getenv("MOTOBUZZ_MOTONETLV_USERNAME")
motonet_password = os.getenv("MOTOBUZZ_MOTONETLV_PASSWORD")

driver_path = r"F:\proga\edgedriver_win64\msedgedriver.exe"

def main():
    product_code = input("Введите код товара: ")

    # Настройки браузера
    options = Options()
    options.use_chromium = True
    service = Service(executable_path=driver_path)
    driver = webdriver.Edge(service=service, options=options)

    # ========== Вкладка 1: Parts Europe ==========
    driver.get("https://partseurope.eu/en/")
    print("Работаем с Parts Europe...")
    run_parts(driver, product_code, parts_username, parts_password)

    # ========== Вкладка 2: Mike Matthies ==========
    driver.execute_script("window.open('');")  # открываем новую вкладку
    driver.switch_to.window(driver.window_handles[-1])
    driver.get("https://mike.matthies.de/en")
    print("Работаем с Mike Matthies...")
    run_mike(driver, product_code, mike_username, mike_password)

    # ========== Вкладка 3: MotonetLV ==========
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get("https://motonetlv.lv")
    print("Работаем с MotonetLV...")
    run_motonet(driver, product_code, motonet_username, motonet_password)

    print("\n✅ Работа завершена. Браузер остаётся открыт.")

    # Ожидаем EXIT от пользователя
    while True:
        cmd = input("Введите команду (напишите EXIT для выхода): ").strip().lower()
        if cmd == "exit":
            print("Закрываем браузер...")
            driver.quit()
            break
        else:
            print("Неизвестная команда. Для выхода введите EXIT.")

if __name__ == "__main__":
    main()
