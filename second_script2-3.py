from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element(By.ID, "num1")
    x1 = element1.text

    element2 = browser.find_element(By.ID, "num2")
    x2 = element2.text

    y = x1=x2

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(y) 

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

