import time
import pytest

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_file


class TestContact:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("contact_data.yml", "test_add_contact"))
    def test_add_contact(self, args):
        name = args["name"]
        phone = args["phone"]

        self.page.contact.click_add_contact()
        self.page.new_contact.input_name(name)
        self.page.new_contact.input_phone(phone)
        self.page.new_contact.click_back()
        assert name == self.page.saved_contect.get_name_title_text()


