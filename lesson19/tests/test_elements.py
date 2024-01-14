import pytest
from selenium.webdriver.remote.webelement import WebElement

from lesson19.DynamicPropertiesPage import PageDynamicProperties
from lesson19.ElementsPage import ElementsPage

@pytest.mark.usefixtures("chrome")
class TestElementsPage:
    def test_page(self, chrome):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert len(elements) == 33

    #  todo перевірити відповіді всіх 33 елементів в елементс
    #  assert elements[2] == "Radio Button"
    @pytest.mark.parametrize("num_elements, result", [
        (0, "Text Box"),
        (1, "Check Box"),
        (2, "Radio Button"),
        (3, "Web Tables"),
        (4, "Buttons"),
        (5, "Links"),
        (6, "Broken Links - Images"),
        (7, "Upload and Download"),
        (8, "Dynamic Properties")
    ] + [(x, "") for x in range(9, 33)])
    def test_page_parametrize(self, chrome, num_elements, result):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert elements[num_elements] == result

    def test_is_button_enabled(self, chrome):
        page = PageDynamicProperties(chrome)
        page.open()
        button: WebElement = page.disable_enable_button()
        button.click()

    def test_is_button_shown(self, chrome):
        page = PageDynamicProperties(chrome).open()  # короткий запис
        button: WebElement = page.button_invisible_visible()
        button.click()
