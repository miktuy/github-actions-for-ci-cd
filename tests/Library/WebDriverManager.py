from page_testing.framework.driver.driver import Driver


class WebDriverManager:
    def __init__(self):
        self._driver: Driver = Driver()

    def start_session_if_not_created(self):
        self._driver.start_session()

    def close_session_if_active(self):
        self._driver.close_session()

    def load_web_page(self, url: str):
        self._driver.get(url)

    def maximize_window(self):
        self._driver.maximaze_window()

    def refresh_page(self):
        self._driver.refresh()

    def turn_off_network(self):
        self._driver.set_network_conditions(
            offline=True, latency=0, throughput=0
        )

    def turn_on_network(self):
        self._driver.set_network_conditions(
            offline=False, latency=0, throughput=0
        )