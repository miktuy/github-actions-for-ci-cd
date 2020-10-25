from page_testing.framework.default_time_settings import ELEMENT_DOES_NOT_EXIST_TIMEOUT_SECONDS
from page_testing.framework.utils.robot_methods import should_be_true
from tests.screens.home import Home


class HomePage:
    def __init__(self):
        self._home_page = Home()

    def check_home_page_is_opened(self):
        is_opened = self._home_page.is_opened(ELEMENT_DOES_NOT_EXIST_TIMEOUT_SECONDS)
        should_be_true(is_opened, "Home page is not opened")