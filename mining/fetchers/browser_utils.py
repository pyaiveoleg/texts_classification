from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


def create_driver() -> WebDriver:
    options = Options()
    # options.add_argument("--headless")
    return webdriver.Firefox(options=options)


class Browser:
    def __init__(self):
        print("[Browser] init")
        self.driver = create_driver()
        self.driver.set_page_load_timeout(10)

    def get_text_elements(self, url: str, css_selector: str) -> List[str]:
        print(f"[Browser] Getting {css_selector} from {url}")
        self.driver.get(url)
        elements = self.driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
        text_elements = [el.text for el in elements]
        print(f"[Browser] Got {len(text_elements)} text elements")
        return text_elements

    def close(self):
        self.driver.close()
