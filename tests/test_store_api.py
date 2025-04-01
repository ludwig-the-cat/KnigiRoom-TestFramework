import requests
from config import STORE_URL
from tests.base_classes.base_response import Response
from src.pydanic_schemas.user import User

def test_getting_user_list(get_user):
    Response(get_user).assert_status_code(200).validate(User)

def test_another():
    assert 1 == 1

