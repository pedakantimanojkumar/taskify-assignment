from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import os
import time


def create_driver():
    """
    If SELENIUM_REMOTE_URL is set, connect to a remote Selenium server (for Docker).
    Otherwise, use a local Chrome browser.
    """
    remote_url = os.environ.get("SELENIUM_REMOTE_URL")

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    if remote_url:
        # In Docker: wait for the Selenium container to be ready
        last_error = None
        for attempt in range(10):
            try:
                return webdriver.Remote(
                    command_executor=remote_url, options=chrome_options
                )
            except Exception as e:
                last_error = e
                print(f"Waiting for Selenium at {remote_url} ({attempt+1}/10): {e}")
                time.sleep(3)
        raise RuntimeError(
            f"Could not connect to Selenium at {remote_url} after multiple attempts"
        ) from last_error

    # Local run, assumes Chrome + chromedriver installed on host
    return webdriver.Chrome(options=chrome_options)


def run_automation():
    driver = create_driver()
    wait = WebDriverWait(driver, 10)

    driver.get("https://demoqa.com/automation-practice-form")

    driver.find_element(By.ID, "firstName").send_keys("Manoj")
    driver.find_element(By.ID, "lastName").send_keys("Kumar")
    driver.find_element(By.ID, "userEmail").send_keys("manoj@test.com")

    gender_label = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='gender-radio-1']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", gender_label)
    driver.execute_script("arguments[0].click();", gender_label)

    driver.find_element(By.ID, "userNumber").send_keys("9876543210")

    driver.find_element(By.ID, "currentAddress").send_keys("Hyderabad, India")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    submit_btn = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].click();", submit_btn)

    time.sleep(2)
    print("Form submitted successfully!")

    driver.quit()


if __name__ == "__main__":
    run_automation()

