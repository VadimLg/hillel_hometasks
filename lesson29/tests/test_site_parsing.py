import pytest
from lesson29.ParsingPage import ParsingPage


@pytest.mark.usefixtures("firefox")
class TestParsingPage:
    def setup(self):
        self.page = ParsingPage(self.driver)

    def test_page(self):
        self.page.open()
        self.page.parsing()
        self.page.click_page(2)
        self.page.parsing()
        pass
