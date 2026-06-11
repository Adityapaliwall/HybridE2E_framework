from config.env import ConfigReader
from pages.login_page import LoginPage
from time import sleep

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

    print("\n===== VALID LOGIN =====")
    print("Login Successful")

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

    print("\n===== INVALID LOGIN =====")
    print("Validation Message Displayed")
