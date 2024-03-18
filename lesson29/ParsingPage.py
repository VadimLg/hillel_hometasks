from datetime import datetime
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

URL = "https://rozetka.com.ua/mobile-phones/c80003/"


class ParsingPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(URL)
        return self

    def parsing(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".goods-tile.ng-star-inserted")
        date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        recording = []
        for element in elements:
            name = element.find_element(By.CSS_SELECTOR, ".goods-tile__title").text
            price = element.find_element(By.CSS_SELECTOR, ".goods-tile__price-value").text
            record = f"Дата: {date}, Найменування: {name}, Ціна: {price} грн.\n"
            recording.append(record)

        with open("result.txt", "a", encoding="utf-8") as file:
            for rec in recording:
                file.write(rec)

    def click_page(self, num_page):
        a_link = self.driver.find_element(By.XPATH, f"//li/a[contains(@href, 'page={num_page}')]")
        if a_link.is_displayed():
            a_link.click()
