from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url="https://www.amazon.in"
def test_amazon():
    driver = webdriver.Chrome(service=(Service(ChromeDriverManager().install())))
    driver.get(url)
    todays_deals = driver.find_element(By.XPATH,"//a[starts-with(text(),'Today')]")
    todays_deals.click()
    clearance_link = driver.find_element(By.XPATH,"//div[@id='nav-subnav']/a[position()=6]")
    clearance_link.click()
    item_link = driver.find_element(By.XPATH,"//a/span[text()='Watches']")
    item_link.click()

    results = driver.find_element(By.XPATH,"//h2[text()='Results']")

    assert "Results" in results.text



