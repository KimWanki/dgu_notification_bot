from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SeleniumRequest(object):
    driver = None
    chrome_options = Options()

    def __init__(self, driver_path, options=None):
        self.driver_path = driver_path
        self.options = ['--headless', '--log-level=3', '--disable-logging', '--no-sandbox', '--disable-gpu']
        self._make_chrome_options(options)
        self.driver = webdriver.Chrome(executable_path=self.driver_path, chrome_options=self.chrome_options)


    def _make_chrome_options(self, options):
        if options is not None:
            self.options += options

        self.chrome_options = Options()
        for opt in set(self.options):
            self.chrome_options.add_argument(opt)

    def get(self, url, callback=None):
        self.driver.get(url)
        return callback(response=self.driver)
