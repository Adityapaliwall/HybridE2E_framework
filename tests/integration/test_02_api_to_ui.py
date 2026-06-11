from config.env import ConfigReader
from pages.login_page import LoginPage
from pages.notes_page import NotesPage
from api.authentication.auth_api import AuthAPI
from api.notes.notes_api import NotesAPI
from utils.read_data import read_json
from utils import logger
from utils.logger import get_logger

logger = get_logger(__name__)


def test_api_to_ui(setup_and_teardown, headers):

    driver = setup_and_teardown
    lp = LoginPage(driver)
    pp = NotesPage(driver)

    ## logning in application throgh api
    print("\n===== API LOGIN =====")
    logger.info("\n===== API LOGIN =====")
    login_payload = read_json("test_data/second_login.json")
    login_response = AuthAPI().login_user(login_payload)
    assert login_response.status_code == 200
    token = login_response.json()["data"]["token"]
    headers = {"x-auth-token": token }
    print("API Login Successful")
    logger.info("API Login Successful")

    ## creating notes through api
    payload = read_json("test_data/delete_note.json")
    title = payload["title"]
    description = payload["description"]

    response = NotesAPI().create_note(headers, payload)
    assert response.status_code == 200
    note_id = response.json()["data"]["id"]

    print("\n===== NOTE CREATED THROUGH API =====")
    print(f"Note ID     : {note_id}")
    print(f"Title       : {title}")
    print(f"Description : {description}")

    logger.info("\n===== NOTE CREATED THROUGH API =====")
    logger.info(f"Note ID     : {note_id}")
    logger.info(f"Title       : {title}")
    logger.info(f"Description : {description}")

    ## delete the note through it id
    print("\n===== DELETE NOTE THROUGH API =====")
    logger.info("\n===== DELETE NOTE THROUGH API =====")
    delete_response = NotesAPI().delete_note( headers, note_id)
    assert delete_response.status_code == 200

    print(f"Status Code : {delete_response.status_code}")
    print(f"Deleted Note ID : {note_id}")
    print("Delete API Successful")

    logger.info(f"Status Code : {delete_response.status_code}")
    logger.info(f"Deleted Note ID : {note_id}")
    logger.info("Delete API Successful")

    ##checking if the notes is really delet or present in the application
    print("\n===== VERIFY DELETION THROUGH API =====")
    logger.info("\n===== VERIFY DELETION THROUGH API =====")
    response = NotesAPI().get_note_by_id(headers,note_id)
    assert response.status_code in [400, 404]
    print("Deleted Note Not Found In API")
    logger.info("Deleted Note Not Found In API")

    ## now logging through ui
    config = ConfigReader.read_config()
    sec_qa = config["second_qa"]
    email = sec_qa["user_email"]
    password = sec_qa["user_password"]

    print("\n===== LOGIN THROUGH UI =====")
    logger.info("\n===== LOGIN THROUGH UI =====")
    lp.scroll_page()
    lp.login(email, password)
    assert lp.is_add_note_visible(), \
        "Login Failed"
    print("UI Login Successful")
    logger.info("UI Login Successful")

    pp.refresh_current_page()

    print("\n===== VERIFY NOTE NOT PRESENT IN UI =====")
    logger.info("\n===== VERIFY NOTE NOT PRESENT IN UI =====")

    all_titles = pp.get_all_note_titles()

    print("Available Notes In UI:")
    logger.info("Available Notes In UI:")

    for note_title in all_titles:
        print(note_title)
    assert title not in all_titles, \
        "Deleted note still visible in UI"

    print(f"\nDeleted Note '{title}' Not Found In UI")
    logger.info(f"\nDeleted Note '{title}' Not Found In UI")