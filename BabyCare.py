
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from WomenEthinic import test_click_baby_care

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver = Chrome()
    driver.get("https://www.meesho.com/")

    try:
        # Wait for the Kids section to be present
        kids_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Kids']"))
        )

        # Hover over the Kids section to reveal the 'All Baby Care' button
        ActionChains(driver).move_to_element(kids_section).perform()
        time.sleep(2)  # Allow some time for the hover effect

        # Wait for the 'All Baby Care' button to be present and clickable
        baby_care_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[4]/div/div[8]/div/div[4]/a/p"))
        )
        baby_care_button.click()
        print("All Baby Care button clicked.")

        time.sleep(2)  # Small delay to see the result of the click

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
          if driver:

               driver.quit()


    test_click_baby_care()
