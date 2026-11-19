from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://books.toscrape.com/"          # a site made for practice

options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")     # uncomment to hide the window
driver = webdriver.Chrome(options=options)
try:
    driver.get(URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "article.product_pod")))
    for book in driver.find_elements(By.CSS_SELECTOR, "article.product_pod")[:5]:
        title = book.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        price = book.find_element(By.CSS_SELECTOR, ".price_color").text
        print(f"{title[:40]:<40} {price}")
    driver.save_screenshot("books.png")
finally:
    driver.quit()