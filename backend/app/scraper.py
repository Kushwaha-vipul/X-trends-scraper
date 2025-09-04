import sys
import os
import time
import requests
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Browserless.io API Key (set env var in Railway)
BROWSERLESS_KEY = os.getenv("BROWSERLESS_API_KEY")
BROWSERLESS_URL = f"wss://production-sfo.browserless.io/webdriver?token={BROWSERLESS_KEY}"

# Backend API URL
BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://localhost:8000/api/trends/")

# ✅ ProxyMesh configuration
PROXY = "http://vipul44:vipul123@us-ca.proxymesh.com:31280"

# Chrome options
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")
options.add_argument(f"--proxy-server={PROXY}")  # 👈 ProxyMesh enabled

# Remote WebDriver (Browserless.io)
driver = webdriver.Remote(
    command_executor=BROWSERLESS_URL,
    options=options
)

wait = WebDriverWait(driver, 20)

try:
    driver.get("https://twitter.com/login")
    print("Opened Twitter login page")
    time.sleep(2)

    username_input = wait.until(EC.element_to_be_clickable((By.NAME, "text")))
    username_input.send_keys("@ScraperX45479")
    time.sleep(2)

    next_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//span[text()="Next"]/ancestor::button[@role="button"]')
    ))
    next_btn.click()
    time.sleep(2)

    try:
        email_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="text"]')))
        email_input.clear()
        email_input.send_keys("vipulkushwaha.2021@gmail.com")

        email_next_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//span[text()="Next"]/ancestor::button[@role="button"]')
        ))
        email_next_btn.click()
    except TimeoutException:
        print("No first email challenge detected, continuing...")

    password_input = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
    password_input.send_keys("Vipul@321")

    login_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//span[text()="Log in"]/ancestor::button[@role="button"]')
    ))
    login_btn.click()

    try:
        verify_email_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="text"]')))
        verify_email_input.clear()
        verify_email_input.send_keys("vipulkushwaha.2021@gmail.com")

        verify_email_next_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//span[text()="Next"]/ancestor::button[@role="button"]')
        ))
        verify_email_next_btn.click()
    except TimeoutException:
        print("No verify email step detected, moving on.")

    wait.until(EC.url_contains("/home"))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="cellInnerDiv"]')))

    script = """
    let elements = document.querySelectorAll('div[data-testid="cellInnerDiv"]');
    let texts = [];
    elements.forEach(el => {
        if (el.innerText.trim() != '') {
            texts.push(el.innerText.trim());
        }
    });
    return texts;
    """

    trends = driver.execute_script(script)
    top_trends = trends[:5]

    print("Top 5 trends:")
    for i, trend in enumerate(top_trends, 1):
        print(f"{i}. {trend}")

    data = {
        "trend1": top_trends[0] if len(top_trends) > 0 else None,
        "trend2": top_trends[1] if len(top_trends) > 1 else None,
        "trend3": top_trends[2] if len(top_trends) > 2 else None,
        "trend4": top_trends[3] if len(top_trends) > 3 else None,
        "trend5": top_trends[4] if len(top_trends) > 4 else None,
        "finished_at": datetime.datetime.utcnow().isoformat(),
        "ip_address": requests.get("https://api.ipify.org").text,
    }

    response = requests.post(BACKEND_API_URL, json=data)
    print(f"Data sent to backend, response status: {response.status_code}")

    time.sleep(20)

finally:
    driver.quit()
    print("Closed browser")
