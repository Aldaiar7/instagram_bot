import time
import random


class WebDriver:
    def __init__(self, driver):
        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, *args, **kwargs):
        time.sleep(100)
        self.driver.close()
        self.driver.quit()
