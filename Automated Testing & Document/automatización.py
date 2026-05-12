from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

usuarios = [
    ("standard_user", "secret_sauce"), #usuario estandar
    ("locked_out_user", "secret_sauce"), #usuario bloqueado
    ("problem_user", "secret_sauce"), #usuario problematico
    ("performance_glitch_user", "secret_sauce"), #
    ("fake_user", "wrong_pass"),  # Usuario Falso
    ("", ""),                     # campos vacíos
]

for usuario, clave in usuarios:
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(clave)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    print(f"Usuario probado: {usuario} | Título de la página: {driver.title}")

driver.quit()