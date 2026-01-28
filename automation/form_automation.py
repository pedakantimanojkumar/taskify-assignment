from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def run_automation():
    driver = webdriver.Chrome()
    try:
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
    finally:
        driver.quit()


if __name__ == "__main__":
    run_automation()

