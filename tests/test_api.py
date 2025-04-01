import requests
from config import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages


def test_getting_data_from_posts():
    r = requests.get(SERVICE_URL)
    r_data = r.json()['products']
    assert r.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(r_data) == 50, GlobalErrorMessages.WRONG_ITEMS_NUMBER.value