from config.env import ConfigReader
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from time import sleep


def test_delete_note(setup_and_teardown):
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
    product = config["delete_note"]
    title = product["title"]
    description = product["dis"]

    pp.create_note(title, description)
    sleep(3)

    # Verify note created
    assert pp.note_exists(title)

    # Delete note

    pp.small_scroll_page()
    sleep(2)
    pp.delete_note()
    sleep(2)

    pp.refresh_current_page()
    sleep(3)

    assert not pp.note_exists(title)

    print("\n===== NOTE DELETED SUCCESSFULLY =====")
    print(f"Deleted Note : {title}")