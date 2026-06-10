from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_BUTTON = (By.XPATH, '//a[.="Login"]')
    EMAIL_FIELD = (By.XPATH, '//input[@data-testid="login-email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@data-testid="login-password"]')
    LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button[@data-testid="login-submit"]')
    ADD_NOTE_BUTTON = (By.XPATH, '//button[contains(. , "Add Note")]')

    def __init__(self, driver):
        super().__init__(driver)

    # Actions
    # def click_login(self):
    #     self.click(self.LOGIN_BUTTON)

    def click_login(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def enter_email(self, email):
        self.enter_text(self.EMAIL_FIELD, email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)

    def click_login_submit(self):
        self.click(self.LOGIN_SUBMIT_BUTTON)

    def click_add_note(self):
        self.click(self.ADD_NOTE_BUTTON)

    def scroll_page(self):
        self.scroll_by_amount(500)

    # Business Action
    def login(self, email, password):
        self.click_login()
        self.scroll_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_submit()

    # Validation
    def is_add_note_visible(self):
        return self.wait.until( lambda driver: driver.find_element(*self.ADD_NOTE_BUTTON) ).is_displayed()