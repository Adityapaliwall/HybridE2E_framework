from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)   ## waiting time for element

    ## element to be clickable
    # def click(self, locator):
    #     self.wait.until(EC.element_to_be_clickable(locator)).click()

    def dismiss_ads(self):
        self.driver.execute_script("""
            document.querySelectorAll('iframe[id^="aswift_"]').forEach(el => el.remove());
            document.querySelectorAll('div.grippy-host').forEach(el => el.remove());
        """)

    def click(self, locator):
        self.dismiss_ads()
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        self.dismiss_ads()

        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def direct_click(self, locator):
        self.driver.find_element(*locator).click()

    ## click at o,o coordiante of the page
    def random_click(self):
        ActionChains(self.driver).move_by_offset(10, 10).click().perform()

    ## ENter text and clear
    def enter_text(self, locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    ## Scroll page
    def scroll_by_amount(self, y):
        ActionChains(self.driver).scroll_by_amount(0, y).perform()

    ## get text from the element
    def get_text(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    ## hovering over the element
    def hovering(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def action_enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).click().send_keys(text).perform()

    def switch_latest_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_to_fisrt_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])


    def switch_frame(self, locator):
        frame = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.switch_to.frame(frame)

    def switch_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    ## Refresh current page
    def refresh_page(self):
        self.driver.refresh()

    def validate_note(self, locator):
        return self.wait.until( EC.visibility_of_element_located(locator) ).text

    def take_screenshot(self, name):
        folder = os.path.join(os.getcwd(), "screenshots")  # To create folder
        os.makedirs(folder, exist_ok=True)
        self.driver.save_screenshot(f"{folder}/screenshot_{name}.png")

    def js_click(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});"
            "arguments[0].click();",
            element
        )



