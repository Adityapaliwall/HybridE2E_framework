from config.env import ConfigReader
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from time import sleep
from utils.read_data import read_json
from utils import logger
from utils.logger import get_logger

logger = get_logger(__name__)

def test_valid_note(setup_and_teardown):
    driver = setup_and_teardown

    lp = LoginPage(driver)
    pp = NotesPage(driver)

    config = ConfigReader.read_config()
    qa = config["qa"]
    email = qa["user_email"]
    password = qa["user_password"]

    lp.scroll_page()
    lp.login(email, password)

    payload = config["product"]
    title = payload["titl"]
    description = payload["dis"]

    pp.create_note(title, description)
    sleep(5)
    note_data = pp.get_note_data()

    assert note_data["title"] == title
    assert note_data["description"] == description

    logger.info("\n-----------valid note created successfully-----------")
    logger.info(f"Title: {title}")
    logger.info(f"Description: {description}")


def test_invalid_note(setup_and_teardown):
    driver = setup_and_teardown

    lp = LoginPage(driver)
    pp = NotesPage(driver)

    config = ConfigReader.read_config()
    qa = config["qa"]
    email = qa["user_email"]
    password = qa["user_password"]

    lp.scroll_page()
    lp.login(email, password)

    invalid = config["invalid_notes"]
    title = invalid["title"]
    description = invalid["dis"]

    pp.create_note(title, description)
    pp.take_screenshot("invalid_note_create.png")

    logger.info("\n_______invalid note test__________")
    logger.info("Screenshot capture")

    pp.click_cancel_note()

