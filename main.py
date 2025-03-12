import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

matsui_id = os.environ.get("MATSUI_ID")
matsui_password = os.environ.get("MATSUI_PASSWORD")

# ChromeDriverのオブジェクトを作成する
driver = webdriver.Chrome()

# Chromeを開いてGoogleにアクセスする
driver.get("https://trade.matsui.co.jp/mgap/login")

login_id = driver.find_element(By.ID, "login-id")
login_id.send_keys(matsui_id)

login_password = driver.find_element(By.ID, "login-password")
login_password.send_keys(matsui_password)

login_password.send_keys(Keys.ENTER)

while driver.current_url != "https://trade.matsui.co.jp/mgap/member":
    time.sleep(3)

time.sleep(3)
future_option_link = driver.find_element(
    By.XPATH, "//li[@data-page='future-option-top']"
)
future_option_link.click()

time.sleep(3)
option_trade_link = driver.find_element(By.XPATH, "//li[@data-page='option-trade']")
option_trade_link.click()

time.sleep(3)
grid_body_price = driver.find_element(By.ID, "grid-body-price")
with open("price.html", "w") as f:
    f.write(grid_body_price.get_attribute("innerHTML"))

time.sleep(3)
risk_indicator_label = driver.find_element(
    By.XPATH, "//label[@for='option-trading-risk']"
)
risk_indicator_label.click()

time.sleep(3)
grid_body_risk = driver.find_element(By.ID, "grid-body-risk")
with open("risk.html", "w") as f:
    f.write(grid_body_risk.get_attribute("innerHTML"))

time.sleep(30)
