from config.env import ConfigReader
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from api.notes.notes_api import NotesAPI
from fixtures.browser_fixture import setup_and_teardown
from utils import logger
from utils.logger import get_logger

logger = get_logger(__name__)

def test_ui_to_api(setup_and_teardown, headers):

    ## setup for the browser and api fxture
    driver = setup_and_teardown
    lp = LoginPage(driver)
    pp = NotesPage(driver)

## reading data form the env files ok
    config = ConfigReader.read_config()
    qa = config["qa"]
    product = config["product"]
    email = qa["user_email"]
    password = qa["user_password"]
    title = product["titl"]
    description = product["dis"]

    ## login through ui interface
    lp.scroll_page()
    lp.login(email, password)
    assert lp.is_add_note_visible()

##  creating notes trough ui

    pp.create_note(title, description)
    pp.refresh_current_page()

    logger.info("===== NOTE CREATED THROUGH UI =====")
    logger.info(f"Title    : {title}")
    logger.info(f"Description : {description}")

    ## validating ui that notes are made or not
    assert pp.valid_note_title() == title
    assert pp.valid_note_content() == description

    ## through api check all notes calling all the notes
    response = NotesAPI().get_all_notes(headers)
    assert response.status_code == 200

    logger.info(f"API Status Code : {response.status_code}")
    response_time = response.elapsed.total_seconds()
    logger.info(f"API Response Time : {response_time:.2f} sec")


    ## search notes recetanly made in api called notes throguh title search
    notes = response.json()["data"]
    found = False
    for note in notes:
        if (
                note["title"] == title and
                note["description"] == description ):
            found = True
            break

    assert found, \
        "Note created in UI not found in API"

    logger.info(f"Total Notes Returned : {len(notes)}")
    logger.info("UI and API Data Matched Successfully")