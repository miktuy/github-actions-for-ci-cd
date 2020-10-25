from selenium.webdriver.common.by import By

from page_testing.framework.base_screen import BaseScreen


class Home(BaseScreen):
    def __init__(self):
        super().__init__(By.CSS_SELECTOR, "div[qa-id='loren-ipsum']")