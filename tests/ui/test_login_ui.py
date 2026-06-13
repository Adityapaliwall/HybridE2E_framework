from config.env import ConfigReader
from pages.login_page import LoginPage
from time import sleep
from utils import logger
from utils.logger import get_logger

logger = get_logger(__name__)

def test_valid_login(setup_and_teardown):

    driver = setup_and_teardown
    lp = LoginPage(driver)
    config = ConfigReader().read_config()
    qa = config["qa"]
    email = qa["user_email"]
    password = qa["user_password"]

    lp.scroll_page()
    lp.login(email,password)
    assert lp.is_add_note_visible(), "Login Failed"

    logger.info("\n===== VALID LOGIN =====")
    logger.info("Login Successful")

def test_invalid_login(setup_and_teardown):
    driver = setup_and_teardown
    lp = LoginPage(driver)
    config = ConfigReader.read_config()
    invalid = config["invalid_qa"]
    email = invalid["user_email"]
    password = invalid["password"]

    lp.scroll_page()
    lp.login(email,password)
    sleep(2)
    lp.take_screenshot("invalid_login")

    assert lp.get_error_message() == "Incorrect email address or password"

    logger.info("\n===== INVALID LOGIN =====")
    logger.info("Validation Message Displayed")
