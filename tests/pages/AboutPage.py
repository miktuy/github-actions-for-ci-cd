from page_testing.framework.default_time_settings import ELEMENT_DOES_NOT_EXIST_TIMEOUT_SECONDS
from page_testing.framework.utils.robot_methods import should_be_true
from tests.screens.about import About


class AboutPage:
    def __init__(self):
        self._about_page = About()

    def check_about_page_is_opened(self):
        is_opened = self._about_page.is_opened(ELEMENT_DOES_NOT_EXIST_TIMEOUT_SECONDS)
        should_be_true(is_opened, "About page is not opened")