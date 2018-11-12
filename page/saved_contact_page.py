from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SavedContactPage(BaseAction):

    name_title = By.ID, "com.android.contacts:id/large_title"

    def get_name_title_text(self):
        return self.get_text(self.name_title)