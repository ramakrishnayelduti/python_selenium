from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--headless")
# options.page_load_strategy = "eager"


driver = webdriver.Chrome(options=options)
driver.get("https://chipsalliance.github.io/caliptra-rtl/main/internal-regs/?p=")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "_Content"))
    )
    innerHTML = driver.execute_script("return document.body.innerHTML")
    print("======================================================================")
    print(driver.page_source)
    print("======================================================================")
    print(innerHTML)
    print("======================================================================")
finally:
    driver.quit()
