import pytest
from lesson28.CheckboxPage import CheckboxPage


@pytest.mark.usefixtures("chrome_class")
class TestCheckboxPage:
    def setup(self):
        self.page = CheckboxPage(self.driver)

    def test_page(self):
        self.page.open()
        self.page.expand_folder_name("home")
        self.page.expand_folder_name("desktop")
        self.page.mark_folder_text("Commands")
        self.page.expand_folder_name("documents")
        self.page.expand_folder_name("office")
        self.page.mark_folder_text("General")
        pass
