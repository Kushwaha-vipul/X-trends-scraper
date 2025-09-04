import sys
import os
import time
import requests
import datetime

from seleniumwire import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Debug: Verify installed versions at runtime
import seleniumwire
import selenium
print("SELENIUMWIRE VERSION:", seleniumwire.__version__)
print("SELENIUM VERSION:", selenium.__version__)

# Backend API URL env var se lo; default local server
BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://localhost:8000/api/trends/")

# Proxy configuration
proxy_options = {
    'proxy': {
        'http': 'http://vipul44:vipul123@us-ca.proxymesh.com:31280',
        'https': 'http://vipul44:vipul123@us-ca.proxymesh.com:31280',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

if sys.platform == "win32":
    # Windows Edge driver with proxy
    edge_options = EdgeOptions()
    driver_path = r"C:\Users\Vipul\Downloads\edgedriver_win64\msedgedriver.exe"
    edge_service = EdgeService(executable_path=driver_path)
    driver = webdriver.Edge(
        seleniumwire_options=proxy_options,
        service=edge_service,
        options=edge_options
    )
else:
    # Linux production - Headless Chrome with proxy
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Environment variables set by Railway / nixpacks
    CHROME_BIN = os.getenv("GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")
    CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")

    # Debug: print chrome paths for verification
    print(f"Chrome binary path: {CHROME_BIN}")
    print(f"Chromedriver path: {CHROMEDRIVER_PATH}")
    print("Chrome binary exists:", os.path.exists(CHROME_BIN))
    print("Chromedriver exists:", os.path.exists(CHROMEDRIVER_PATH))

    chrome_options.binary_location = CHROME_BIN
    chrome_service = ChromeService(executable_path=CHROMEDRIVER_PATH)

    driver = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
        seleniumwire_options=proxy_options
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

    time.sleep(50)

finally:
    driver.quit()
    print("Closed browser")
