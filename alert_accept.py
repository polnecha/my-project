from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/alert_accept.html")

# Нажимаем кнопку
browser.find_element(By.CSS_SELECTOR, "button").click()

# Принимаем confirm
browser.switch_to.alert.accept()

# Получаем число
x = browser.find_element(By.ID, "input_value").text

# Решаем задачу
y = str(math.log(abs(12 * math.sin(int(x)))))

# Вводим ответ
browser.find_element(By.ID, "answer").send_keys(y)

# Отправляем ответ
browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Оставляем браузер открытым
input("Скопируй ответ и нажми Enter...")

browser.quit()
