import pytest
from lesson29.ParsingPage import ParsingPage


@pytest.mark.usefixtures("firefox")
class TestCheckboxPage:
    def setup(self):
        self.page = ParsingPage(self.driver)

    def test_page(self):
        self.page.open()
        self.page.parsing()
        self.page.next_page(2)
        self.page.parsing()
        pass
