import pytest
import os
from selenium.webdriver import Chrome, ChromeOptions
from config.env import ConfigReader


@pytest.fixture(scope="function")
def setup_and_teardown():
    ## Read env and config file
    config = ConfigReader.read_config()
    env = config["qa"]
    base_url = env["base_url"]

    # Setup
    o = ChromeOptions()
    o.add_experimental_option("detach", True)  # Keep browser open
    o.add_argument("--no-sandbox")
    o.add_argument("--disable-notifications")
    o.add_argument("--start-maximized")
    o.add_argument("--disable-popup-blocking")
    o.add_argument("--disable-blink-features=AutomationControlled")
    o.add_argument("--disable-notifications")
    o.add_argument("--disable-popup-blocking")
    o.add_argument("--disable-blink-features=AutomationControlled")
    o.add_argument("--disable-features=InterestFeedContentSuggestions")
    o.add_argument("--disable-background-networking")
    o.add_argument("--disable-background-timer-throttling")
    o.add_argument("--disable-renderer-backgrounding")
    # o.add_argument("--headless=new")


    driver = Chrome(options=o)

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(base_url)

    yield driver

    # Teardown
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:

        driver = item.funcargs.get("setup_and_teardown")

        if driver:
            folder = os.path.join(os.getcwd(), "screenshots")  # To create folder
            os.makedirs(folder, exist_ok=True)
            driver.save_screenshot(f"{folder}/screenshot_{item.name}.png")

            print(f"\nScreenshot Saved: "f"screenshot_{item.name}.png")

