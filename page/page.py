from page.contact_page import ContactPage
from page.new_contact_page import NewContactPage
from page.saved_contact_page import SavedContactPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def contact(self):
        return ContactPage(self.driver)

    @property
    def new_contact(self):
        return NewContactPage(self.driver)

    @property
    def saved_contect(self):
        return SavedContactPage(self.driver)

