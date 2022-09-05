import selenium
import os
import time
import random

from auth import login, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from modules import WebDriver


def search_by_hashtag(hashtag, driver):

    driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
    for _ in range(1, 4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randrange(2, 5))
    hrefs = driver.find_elements(By.TAG_NAME, "a")

    urls = [
        item.get_attribute("href")
        for item in hrefs
        if "/p/" in item.get_attribute("href")
    ]
    print(urls)
    for url in urls:
        driver.get(url)
        time.sleep(random.randrange(3, 5))
        like = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button",
        )
        like.click()
        time.sleep(random.randrange(85, 105))


def open_firefox(login, password):
    with WebDriver(
        webdriver.Firefox(
            executable_path=os.getenv("executable_path")
        )
    ) as browser:
        browser.implicitly_wait(5)
        browser.get("https://www.instagram.com")

        time.sleep(random.randrange(2, 7))

        _login = browser.find_element(By.NAME, "username")
        _login.clear()
        _login.send_keys(login)

        time.sleep(random.randrange(2, 7))

        _password = browser.find_element(By.NAME, "password")
        _password.clear()
        _password.send_keys(password)

        time.sleep(random.randrange(2, 7))

        _button = browser.find_element(By.CSS_SELECTOR, ".L3NKy > div:nth-child(1)")
        _button.click()
        time.sleep(5)
        search_by_hashtag("ferrari", browser)


def main():
    open_firefox(login, password)


if __name__ == "__main__":
    main()
