import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service = Service(r"/Users/g5/GitRep" + "chromedriver")
    )

    # відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys("vitaliikots@mistakeinemail.com")
    
    # знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # вводимо неправильний пароль
    pass_elem.send_keys("wrong password")
    
    # знаходимо кнопку Sign In
    btn_elem = driver.find_element(By.NAME, "commit")

    # емулюємо клік лівою кнопкою мишки
    btn_elem.click()
    
    # перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"

    # закриваємо браузер 
    driver.close()
