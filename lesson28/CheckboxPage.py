from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

URL = "https://demoqa.com/checkbox"


class CheckboxPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(URL)
        return self

    def expand_folder_name(self, name) -> None:
        checkbox_button = self.driver.find_element(By.XPATH,
                                                   f"//label[contains(@for, 'tree-node-{name}')]//ancestor::span/button")
        try:
            expand = checkbox_button.find_element(By.XPATH,
                                                  f"//label[contains(@for, 'tree-node-{name}')]//ancestor::span//*[contains(@class, 'expand-open')]")
            if expand.is_displayed():
                expand.click()
        except NoSuchElementException:
            pass
        checkbox_button.click()

    def mark_folder_text(self, text):
        checkbox_button = self.driver.find_element(By.XPATH, f"//*[text()='{text}']//ancestor::label")
        input_field = self.driver.find_element(By.XPATH, f"//*[text()='{text}']//ancestor::label/input")
        if not input_field.is_selected():
            checkbox_button.click()
