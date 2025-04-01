from http.client import responses

import pytest
import requests

from config import STORE_URL


@pytest.fixture(scope='function', autouse=True)
def get_user():
    response = requests.get(STORE_URL)
    return response