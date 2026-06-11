from config.env import ConfigReader
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from time import sleep


def test_edit_note(setup_and_teardown):
    driver = setup_and_teardown
    lp = LoginPage(driver)
    pp = NotesPage(driver)

    config = ConfigReader.read_config()
    qa = config["qa"]
    email = qa["user_email"]
    password = qa["user_password"]

    lp.scroll_page()
    lp.login(email, password)

    # Create note first
    product = config["product"]
    old_title = product["titl"]
    old_description = product["dis"]

    pp.create_note(old_title,old_description)
    sleep(5)

    # Edit note
    edit_data = config["edit_note"]
    new_title = edit_data["title"]
    new_description = edit_data["dis"]

    pp.small_scroll_page()
    sleep(2)
    pp.edit_note(new_title,new_description)
    sleep(3)
    note_data = pp.get_note_data()

    assert note_data["title"] == new_title
    assert note_data["description"] == new_description

    print("\n===== NOTE UPDATED SUCCESSFULLY =====")
    print(f"Title       : {new_title}")
    print(f"Description : {new_description}")


def test_edit_note_invalid_title(setup_and_teardown):
    driver = setup_and_teardown
    lp = LoginPage(driver)
    pp = NotesPage(driver)

    config = ConfigReader.read_config()
    qa = config["qa"]
    email = qa["user_email"]
    password = qa["user_password"]

    lp.scroll_page()
    lp.login(email, password)

    # Create note first
    product = config["product"]
    old_title = product["titl"]
    old_description = product["dis"]

    pp.create_note(old_title,old_description)
    sleep(5)

    # Invalid edit
    invalid = config["invalid_edit_note"]
    title = invalid["title"]
    description = invalid["dis"]

    pp.small_scroll_page()
    sleep(2)
    pp.edit_note(title,description)
    sleep(3)

    pp.take_screenshot("invalid_edit_note")
    print("\n===== INVALID EDIT TEST =====")
    print("Screenshot Captured")

    pp.click_cancel_note()