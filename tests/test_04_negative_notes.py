from config.env import ConfigReader
from pages.notes_page import NotesPage
from pages.login_page import LoginPage


def test_invalid_note(setup_and_teardown):

    driver = setup_and_teardown

    pp = NotesPage(driver)
    lp = LoginPage(driver)

    config = ConfigReader.read_config()
    qa = config["qa"]
    email = qa["user_email"]
    password = qa["user_password"]

    lp.scroll_page()
    lp.login(email, password)

    assert lp.is_add_note_visible()
    config = ConfigReader.read_config()
    inv = config["invalid_notes"]
    title = inv["title"]
    description = inv["dis"]

    pp.small_scroll_page()
    pp.click_on_add_note()
    pp.enter_title(title)
    pp.enter_description(description)
    pp.click_create()
    pp.take_screenshot("invalid_note")

    print("\nInvalid Note Screenshot Captured")
    pp.click_cancel_note()