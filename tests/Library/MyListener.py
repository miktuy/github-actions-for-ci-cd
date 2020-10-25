from robot.model import Message

from page_testing.framework.driver.driver import Driver


class MyListener:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LISTENER_API_VERSION = 3
    LOG_MESSAGE_LEVELS = {'WARN', 'ERROR', 'FAIL'}

    def _set_driver(self):
        self._driver = Driver()

    def __init__(self) -> None:
        self.ROBOT_LIBRARY_LISTENER = self

    def _log_message(self, message: Message) -> None:
        self._set_driver()
        if message.level in self.LOG_MESSAGE_LEVELS:
            self._driver.take_screenshot()

    def _close(self):
        self._set_driver()
        """ Closes all browser windows and terminate webdriver
        when the whole tests execution ends """
        self._driver.quit()