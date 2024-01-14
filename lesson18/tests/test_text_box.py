from lesson18.TextBoxPage import TextBoxPage


class TestTextBox:
    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Pavlo")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_fullname()
        assert name_field.replace("Name:", "") == "Pavlo"

    def test_email_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_email_field("email@gmail.com")
        page.scroll_down()
        page.click_submit()
        email_field = page.get_result_email()
        assert email_field.replace("Email:", "") == "email@gmail.com"

    def test_curr_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_current_address_field("test current address")
        page.scroll_down()
        page.click_submit()
        curr_addr_field = page.get_result_current_address()
        assert curr_addr_field.replace("Current Address :", "") == "test current address"

    def test_perm_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_permanent_address_field("test permanent address")
        page.scroll_down()
        page.click_submit()
        perm_addr_field = page.get_result_permanent_address()
        assert perm_addr_field.replace("Permananet Address :", "") == "test permanent address"