from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NotesPage(BasePage):

    check_box = (By.XPATH, '//input[@id="completed"]')
    title_box = (By.XPATH, '//input[@id="title"]')
    description_box = (By.XPATH, '//textarea[@id="description"]')

    create_button = (By.XPATH, '//button[.="Create"]')
    view_button = (By.XPATH, '//a[.="View"]')
    edit_button = (By.XPATH, '//a[.="Edit"]')
    delete_button = (By.XPATH, '(//button[.="Delete"])[1]')
    cancel_note_button = (By.XPATH, '//button[contains(. , "Cancel")]')

    confirm_delete_button = (By.XPATH, '//button[@data-testid="note-delete-confirm"]')

    category_select = (By.XPATH, '//select[@id="category"]')

    success_message = (By.XPATH, "//div[contains(@class,'alert')]")
    valid_note_title_text = (By.XPATH, '(//div[contains(@class , "card-header fw-bold text-truncate")])[1]')

    valid_note_content_text = (By.XPATH, '(//p[contains(@class , "card-text")])[1]')
    add_note_button = (By.XPATH, '//button[contains(. , "Add Note")]')

    def __init__(self, driver):
        super().__init__(driver)

    # Actions

    def click_check_box(self):
        self.click(self.check_box)

    def small_scroll_page(self):
        self.scroll_by_amount(100)

    def enter_title(self, title):
        self.enter_text(self.title_box, title)

    def enter_description(self, description):
        self.enter_text(self.description_box, description)

    def click_create(self):
        self.click(self.create_button)

    def click_view(self):
        self.click(self.view_button)

    def click_edit(self):
        self.click(self.edit_button)

    def click_delete(self):
        self.click(self.delete_button)

    def click_confirm_delete(self):
        self.click(self.confirm_delete_button)

    def refresh_current_page(self):
        self.refresh_page()

    def click_on_add_note(self):
        self.click(self.add_note_button)

    def click_cancel_note(self):
        self.click(self.cancel_note_button)

    # Business Methods

    def create_note(self, title, description):
        self.enter_title(title)
        self.enter_description(description)
        self.click_create()

    def delete_note(self):
        self.click_delete()
        self.click_confirm_delete()

    # Validations

    def note_exists(self, title):
        xpath = f"//*[contains(text(),'{title}')]"
        return len(self.driver.find_elements(By.XPATH, xpath)) > 0

    def get_success_message(self):
        return self.get_text(self.success_message)

    def valid_note_title(self):
        return self.validate_note(self.valid_note_title_text)

    def valid_note_content(self):
        return self.validate_note(self.valid_note_content_text)

    def get_note_data(self):
        return {
            "title": self.valid_note_title(),
            "description": self.valid_note_content()
        }

    def get_all_note_titles(self):
        elements = self.driver.find_elements(By.XPATH,'//div[contains(@class,"card-header")]')
        return [element.text for element in elements]

