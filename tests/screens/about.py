from selenium.webdriver.common.by import By

from page_testing.framework.base_screen import BaseScreen


class About(BaseScreen):
    def __init__(self):
        super().__init__(By.CSS_SELECTOR, "p[qa-id='simple-about-string']")